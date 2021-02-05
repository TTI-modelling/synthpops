"""Examples for the age demographics from the 4th schools report."""
import numpy as np
import sciris as sc
import synthpops as sp
import matplotlib as mplt
import matplotlib.pyplot as plt
import cmasher as cmr
import cmocean as cmo
import os


mplt.rcParams['font.family'] = 'Roboto Condensed'  # Pretty font being set
mplt.rcParams['font.size'] = 16


# population parameters
pars = sc.objdict(
    n                               = 200e3,
    rand_seed                       = 123,

    country_location                = 'usa',
    state_location                  = 'Washington',
    location                        = 'seattle_metro',
    use_default=True,

    household_method                = 'fixed_ages',
    smooth_ages                     = 1,

    with_facilities                 = 1,
    with_non_teaching_staff         = 1,
    with_school_types               = 1,


    school_mixing_type              = {'pk': 'age_and_class_clustered',
                                       'es': 'age_and_class_clustered',
                                       'ms': 'age_and_class_clustered',
                                       'hs': 'random', 'uv': 'random'},
    average_student_teacher_ratio   = 20,  # location specific
    average_student_all_staff_ratio = 11,  # from Seattle Public Schools
)

kwargs = sc.dcp(pars)  # plotting parameters

colors = dict(
    seattle_metro   = 'tab:green',
    Spokane_County  = 'tab:purple',
    Franklin_County = 'tab:red',
    Island_County   = 'tab:blue',
)

labels = dict(
    seattle_metro   = 'Seattle',
    Spokane_County  = 'Spokane',
    Franklin_County = 'Franklin',
    Island_County   = 'Island',
)


locations = ['seattle_metro', 'Spokane_County', 'Franklin_County', 'Island_County']

x = np.arange(101)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.subplots_adjust(left=0.10, right=0.93, top=0.9, bottom=0.13)

for n, location in enumerate(locations):
    # pars.location = location

    loc_pars = dict(location=location, state_location=pars.state_location, country_location=pars.country_location,
                    datadir=sp.datadir, window_length=7)

    expected_age_distr = sp.get_smoothed_single_year_age_distr(**loc_pars)

    y = [expected_age_distr[a] * 100 for a in x]
    ax.plot(x, y, color=colors[location], label=labels[location], marker='o', markerfacecolor=colors[location],
            markeredgecolor='white', markeredgewidth=1, markersize=6,)
leg = ax.legend(loc = 1)

ax.set_xlim(0, 100)
ax.set_ylim(0, 2.0)
ax.set_xlabel('Age', fontsize=16)
ax.set_ylabel('(%)', fontsize=16)
ticks = np.arange(0, 101, 10)
ticklabels = [str(i) for i in ticks]
ax.set_xticks(ticks)
ax.set_xticklabels(ticklabels)
ax.set_title('Age Distribution', fontsize=20)

# ax.set_xticklabels(np.arange(0, 101, 10), [str(i) for i in np.arange(0, 101, 10)])
ax.tick_params(labelsize=15)
# plt.show()
fig.savefig('schools_report_4_age_demographics.png', format='png', dpi=150)
fig.savefig('AgeDistributionsbyLocation.png', format='png', dpi=150)