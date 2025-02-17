import synthpops as sp
import settings
import random
import pytest
from synthpops import workplaces as spw
from synthpops.workplaces import Workplace
import sciris as sc


@pytest.fixture(scope="module")
def create_small_pop():
    return sp.Pop(n=settings.pop_sizes.small)


@pytest.fixture(scope="module")
def create_adult_pools(create_small_pop):
    return ((k, v['age']) for k, v in create_small_pop.popdict.items() if v['age'] > 20)


def get_adults(create_adult_pools, n=1):
    adult_gen = create_adult_pools
    i = 0
    total = n
    for a in adult_gen:
        yield a
        next(adult_gen)
        i += 1
        if i >= n:
            break


def test_initialize_empty_workplaces(create_small_pop):
    pop = sc.dcp(create_small_pop)
    for n in [0, 5]:
        spw.initialize_empty_workplaces(pop, n_workplaces=n)
        assert len(pop.workplaces) == pop.n_workplaces == n


def test_make_workplace(create_small_pop):
    pop = sc.dcp(create_small_pop)
    work = spw.Workplace()
    x = random.randint(0, len(pop.workplaces)-1)
    params = sc.objdict(wpid=pop.workplaces[x]['wpid'],
                        member_uids=pop.workplaces[x]['member_uids'])
    work.set_layer_group(**params)
    for i in params:
        errmsg = f"{i} not equal!, expected: {pop.workplaces[x][i]} actual: {work[i]}"
        if hasattr(work[i], "__len__"):
            assert len(work[i]) == len(pop.workplaces[x][i]), errmsg
        else:
            assert work[i] == pop.workplaces[x][i], errmsg

def test_populate_workplaces(create_small_pop, create_adult_pools):
    pop = sc.dcp(create_small_pop)
    original_workplace_n = len(pop.workplaces)
    # populate fewer or more workplaces
    for n in [min(5, len(pop.workplaces)), max(5, len(pop.workplaces))+1]:
        workplaces = []
        for i in range(0, n):
            workplaces.append([j[0] for j in list(get_adults(create_adult_pools, random.randint(1, 3)))])
            spw.populate_workplaces(pop, workplaces)
        current_workplace_n = len(pop.workplaces)
        print(f"before: {original_workplace_n} after {current_workplace_n}")
        # the populated ones should be replaced
        for i in range(0, len(workplaces)):
            assert set(pop.workplaces[i]['member_uids']) == set(workplaces[i]), f"{i}th workplace not populated."


def test_add_workplace(create_small_pop, create_adult_pools):
    pop = sc.dcp(create_small_pop)
    max_pid = max([i['wpid'] for i in pop.workplaces])
    new_workers = [i for i in list(get_adults(create_adult_pools, random.randint(3, 5)))]
    param = {'member_uids': new_workers[0],
             'wpid': max_pid+1}
    workplace = Workplace(**param)
    pop = create_small_pop
    spw.add_workplace(pop, workplace)
    assert pop.workplaces[-1] == workplace


def test_validate_workplace(create_small_pop):
    # check for invalid parameters
    param = {'member_uids': [1],
             'wpid': 1}
    invalidparam1 = param.copy()
    invalidparam1['wpid'] = "w1"
    with pytest.raises(TypeError):
        workplace = Workplace(**invalidparam1)
    invalidparam2 = param.copy()
    invalidparam2['member_uids'] = ["w1"]
    with pytest.raises(TypeError):
        workplace = Workplace(**invalidparam2)


def test_get_workplace(create_small_pop):
    pop = create_small_pop
    # randomly pick wpid
    wpid = random.choice([i['wpid'] for i in pop.workplaces])
    # check if workplace matches
    workplace = spw.get_workplace(pop, wpid)
    assert workplace['wpid'] == wpid
    workers_age = [pop.popdict[k]['age'] for k in workplace['member_uids']]
    assert set(workers_age) == set(workplace.member_ages(pop.age_by_uid))


def test_get_workplace_invalid(create_small_pop):
    pop = create_small_pop
    max_pid = max([i['wpid'] for i in pop.workplaces])
    with pytest.raises(IndexError):
        spw.get_workplace(pop, max_pid+1)
