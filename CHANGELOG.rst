==========
What's new
==========

Starting with SynthPops version 1.5.2, this file will document all changes to the codebase. By nature, SynthPops is a library to generate stochastic networked populations, so over time there will be model and code updates that change regression results. When these kinds of changes are made, we'll flag that here with the term "Regression Information". In addition, here are some other terms useful for understanding updates documented here.


~~~~~~~~~~~~~~~~~~~~
Legend for changelog
~~~~~~~~~~~~~~~~~~~~

- "Feature": a new feature previously unavailable.

- "Efficiency": a refactor of a previous method to make the calculation faster or require less memory.

- "Fix": a fix to a bug in the code base where a method either did not work under certain conditions or results were not as expected.

- "Deprecated": a method or feature that has been removed or support will be removed for in the future.

- "Regression Information": a change to the model or update to data resulted in a change to regression results.

- "Github Info": the associated PRs to any changes.


~~~~~~~~~~~~~~~~~~~~~~~
Latest versions (1.8.x)
~~~~~~~~~~~~~~~~~~~~~~~


Version 1.8.0 (2021-05-07)
--------------------------
- This is a big one!
- *Feature*: Class structures implemented for each layer and added to pop objects generated via `pop = sp.Pop()`. For example, now you can do ``pop.get_household(i)`` to get the household with integer ``hhid`` with value ``i`` which will be a ``sp.Household`` object with at minimum the attributes ``hhid``, ``member_uids``, ``reference_uid``, and ``reference_age``.
- Base class for layer groups available in ``sp.base.py``; see class ``sp.base.LayerGroup()`` for more info. Important to note that this class has a method ``member_ages()`` which takes in a mapping of person ids to age to return the ages of individuals in a layer group. Optional parameter `subgroup_member_uids` allows you to return the ages for a subgroup of individuals.
- The specific layer classes implemented are ``sp.Household``, ``sp.School``, ``sp.Classroom``, ``sp.Workplace``, ``sp.LongTermCareFacility``. Each is based off of ``sp.LayerGroup``.
- Class also added for classroom structures in schools when schools are strictly cohorted into classrooms (school_mixing_type equals 'age_and_class_clustered').
- Method name changes: ``sp.get_age_by_brackets_dic()`` -> ``sp.get_age_by_brackets()``, ``sp.get_index_by_brackets_dic()`` -> ``sp.get_index_by_brackets()``, ``sp.get_ids_by_age_dic()`` -> ``sp.get_ids_by_age()``, ``sp.make_contacts_from_microstructure_objects()`` -> ``sp.make_contacts()``, ``sp.get_contact_matrix_dic()`` -> ``sp.get_contact_matrices()``, 
- ``sp.make_contacts()`` now returns a tuple; a dictionary version of the population and a dictionary version of schools to identify classrooms and other other groupings in schools. These are then used to populate the school and classroom structures in ``sp.Pop.generate()``.
- *Regression Information*: Attribute names related to Long Term Care Facilities have changed to be more consistent with class name; ``snfid`` -> ``ltcfid``, ``snf_res`` -> ``ltcf_res``, ``snf_staff`` -> ``ltcf_staff``.
- *Github*: PR `347 <https://github.com/amath-idm/synthpops/pull/347>`__


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Versions 1.7.x (1.7.0 – 1.7.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Version 1.7.7 (2021-05-07)
--------------------------
- Made changes to allow SynthPops to be installed via ``pip``.
- Updated examples in the folder ``synthpops/examples``.
- Most significantly, changed the default data folder from ``synthpops/data`` to ``synthpops/synthpops/data``.
- *Github*: PRs: `465 <https://github.com/amath-idm/synthpops/pull/465>`__


Version 1.7.6 (2021-05-05)
--------------------------
- Updated random graph model to use networkx's fast Erdos-Renyi graph generator implementation, which speeds up generation time for the model.
- *Regression Information*: The fast Erdos Renyi graph implementation changes the edges chosen, though not the statistical properties of the degree distribution.
- *Github*: PRs: `449 <https://github.com/amath-idm/synthpops/pull/449>`__


Version 1.7.5 (2021-05-03)
--------------------------
- ``sp.contact_networks.get_contact_counts_by_layer()`` now returns two dictionaries, one that gives the number of contacts between different roles in settings, like the number of contacts for students to teachers in schools, as well as the number of contacts per group in a setting, for example the number of contacts people have in the workplace with `wpid == 0`.
- ``sp.sampling.statistic_test()`` with `verbose = True` prints to screen details about the expected and actual distributions when the test fails. 
- *Fix*: Default `n` value now assigned in ``sp.defaults.py`` when ``sp.Pop`` supplied `n = None` and when `n` is lower than ``sp.defaults.default_pop_size``
- *Github*: PRs `435 <https://github.com/amath-idm/synthpops/pull/435>`__, `448 <https://github.com/amath-idm/synthpops/pull/448>`__


Version 1.7.4 (2021-04-21)
--------------------------
- *Feature*: new summary information added to pop objects: ``pop.summary.average_age``, ``pop.summary.layer_degrees``, ``pop.summary.layer_stats``, and ``pop.summary.layer_degree_description``, using the pandas DataFrame describe method. These give information on the overall degree distribution as well as the degree distribution by age for different layers generated using synthpops. Methods added to calculate these are generalized so in principle if other layers are added to the population post hoc or if connections change, these information can be re-calculated.
- Also added is ``pop.summarize()`` which will print to screen and return a string of a brief description of the population generated using SynthPops.
- *Github* : PR `442 <https://github.com/amath-idm/synthpops/pull/442>`__ 


Version 1.7.3 (2021-04-16)
--------------------------
- *Fix*: Restructured how default location parameters are stored; now moved from ``sp.config.py`` into a dictionary available from ``sp.defaults.py``. Methods added in ``sp.defaults.py`` to reset these values to user specified information.
- *Deprecated*: ``sp.get_config_data()`` is no longer available. The data returned from that method are now simply stored as a dictionary available as ``sp.defaults.default_data``. Previous globally available parameters, most of which were not in use: ``sp.datadir``, ``sp.localdatadir``, ``sp.rel_path``, ``sp.alt_rel_path``, ``sp.default_country``, ``sp.default_state``, ``sp.default_location``, ``sp.default_sheet_name``, ``sp.alt_location``, ``sp.default_household_size_1_included``, are either now stored in and accesible via ``sp.defaults.py`` or removed from use.
- *Github*: PRs `436 <https://github.com/amath-idm/synthpops/pull/436>`__, `438 <https://github.com/amath-idm/synthpops/pull/438>`__


Version 1.7.2 (2021-04-13)
--------------------------
- *Feature*: Re-enabled support of age distributions for any number of age brackets. Json data files have been updated to accomodate this flexibility.
- *Fix*: Catching division by zero when calculating enrollment, employment, etc. rates by age and the number of people in a given age is zero (can occur when population size is very small, e.g. n~200).
- *Github Info*: PRs `401 <https://github.com/amath-idm/synthpops/pull/401>`__, `422 <https://github.com/amath-idm/synthpops/pull/422>`__


Version 1.7.1 (2021-04-09)
--------------------------
- *Feature*: Added checks for probability distributions with methods ``sp.check_all_probability_distribution_sums()``, ``sp.check_all_probability_distrubution_nonnegative()``, ``sp.check_probability_distribution_sum()``, ``sp.check_probability_distribution_nonnegative()``. These check that probabilities sum to 1 within a tolerance level  (0.05), and have all non negative values. Added method to convert data from pandas dataframe to json array style, ``sp.convert_df_to_json_array()``. Added statistical test method ``sp.statistic_test()``. Added method to count contacts, ``sp.get_contact_counts_by_layer()``, and method to plot the results, ``sp.plot_contact_counts()``. See ``sp.contact_networks.get_contact_counts_by_layer()`` for more details on the method.
- Added example of how to load data into the location json objects and save to file. See ``examples/create_location_data.py`` and ``examples/modify_location_data.py``.
- *Github Info*: PRs `410 <https://github.com/amath-idm/synthpops/pull/410>`__, `413 <https://github.com/amath-idm/synthpops/pull/413>`__, `423 <https://github.com/amath-idm/synthpops/pull/423>`__


Version 1.7.0 (2021-04-05)
--------------------------
- *Efficiency*: Major refactor of data methods to read from consolidated json data files for each location and look for missing data from parent locations or alternatively json data files for default locations. Migration of multiple data files for locations into a single json object per location under the ``data`` directory. This will should make it easier to identify all of the available data per location and where missing data are read in from. Examples of how to create, change, and save new json data files will come in the next minor version update.
- *Feature*: Location data jsons now have fields for the data source, reference links, and citations! These fields will be fully populated shortly. Please reference the links provided for any data obtained from SynthPops as most population data are sourced from other databases and should be referenced as such.
- *Deprecated*: Refactored data methods no longer support the reading in of data from user specified file paths. Use of methods to read in age distributions aggregated to a number of age brackets not equal to 16, 18, or 20 (officially supported values) is currently turned off. Next minor update will re-enable these features. Old methods are available in `synthpops.data_distributions_legacy.py`, however this file will be removed in upcoming versions once we have migrated all examples to use the new data methods and have fully enabled all the functionality of the original data methods. Please update your usage of SynthPops accordingly.
- Updated documentation about the input data layers.
- *Github Info*: PRs `407 <https://github.com/amath-idm/synthpops/pull/407>`__, `303 <https://github.com/amath-idm/synthpops/pull/303>`__


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Versions 1.6.x (1.6.0 – 1.6.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Version 1.6.2 (2021-04-01)
--------------------------
- *Feature*: Added new methods, ``sp.get_household_head_ages_by_size()``, ``sp.plot_household_head_ages_by_size()``. Also accessible pop methods as ``pop.get_household_head_ages_by_size()``, ``pop.plot_household_head_ages_by_size()``. These calculate the generated count the household head age by the household size, and the plotting methods compare this to the expected age distributions by size as matrices.
- *Github Info*: PR `385 <https://github.com/amath-idm/synthpops/pull/385>`__


Version 1.6.1 (2021-03-25)
--------------------------
- *Feature*: Added new methods, ``sp.check_dist()`` and aliases ``sp.check_normal()`` and ``sp.check_poisson()``, to check whether the observed distribution matches the expected distribution.
- *Github Info*: PR `373 <https://github.com/amath-idm/synthpops/pull/373>`__


Version 1.6.0 (2021-03-20)
--------------------------
- *Feature*: Adding summary methods for SynthPops pop objects accesible as pop.summary and computed using pop.compute_summary(). Also adding several plotting methods for these summary data.
- Updating ``sp.workplaces.assign_rest_of_workers()`` to work off a copy of the workplace age mixing matrix so that the copy stored in SynthPops pop objects is not modified during generation.
- More tests for summary methods in pop.py, methods in config.py, plotting methods in plotting.py
- *Regression Information*: Adding new workplace size data specific for the Seattle metro area which changes the regression results. The previous data from the Washington state level and the new data for the metropolitan statistical area (MSA) of Seattle for the 2019 year are very similar, however the use of this data with random number generators does result in slight stochastic differences in the populations generated. 
- *Github Info*: PRs `356 <https://github.com/amath-idm/synthpops/pull/356>`__, `357 <https://github/com/amath-idm/synthpops/pull/357>`__, `358 <https://github.com/amath-idm/synthpops/pull/358>`__, `360 <https://github.com/amath-idm/synthpops/pull/360>`__



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Versions 1.5.x (1.5.2 – 1.5.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Version 1.5.3 (2021-03-16)
--------------------------
- *Deprecated*: Removing use of verbose parameter to print statements to use logger.debug() instead and removing the verbose parameter where deprecated.
- *Github Info*: PRs `363 <https://github.com/amath-idm/synthpops/pull/363>`__, `379 <https://github.com/amath-idm/synthpops/pull/379>`__, `380 <https://github.com/amath-idm/synthpops/pull/380>`__


Version 1.5.2 (2021-03-09)
--------------------------
- *Feature*: Added metadata to pop objects.
- Updated installation instructions and reference citation.
- *Github Info*: PRs `365 <https://github.com/amath-idm/synthpops/pull/365>`__, `351 <https://github.com/amath-idm/synthpops/pull/351>`__



