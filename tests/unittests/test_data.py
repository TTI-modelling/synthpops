import synthpops as sp

import unittest

class TestLocation(unittest.TestCase):

    def minimal_test_str(self):
        test_str = """{
          "data_provenance_notices": ["notice1","notice2"],
          "reference_links": ["reference1","reference2"],
          "citations": ["citation1","citation2"],
          "population_age_distribution": [
            [0,4,0.06],
            [5,9,0.20]
          ],
          "employment_rates_by_age": [
            [19,0.300],
            [20,0.693]
          ],
          "enrollment_rates_by_age": [
            [2,0],
            [3,0.529]
          ],
          "household_head_age_brackets": [
            [18,19],
            [20,24]
          ],
          "household_head_age_distribution_by_family_size": [
            [2,163,999],
            [3,115,757]
          ],
          "household_size_distribution": [
            [1,0.2781590909877753],
            [2,0.3443313103056699]
          ],
          "ltcf_resident_to_staff_ratio_distribution": [
            [1,1,0.0],
            [2,2,5.0]
          ],
          "ltcf_num_residents_distribution": [
            [0,19,0.0],
            [20,39,0.08955223880597014]
          ],
          "ltcf_num_staff_distribution": [
            [0,19,0.014925373134328358],
            [20,39,0.07462686567164178]
          ],
          "school_size_distribution": [
            [20,50,0.027522935779816515],
            [51,100,0.009174311926605505]
          ],
          "school_types_by_age": [
            {
              "school_type": "pk-es",
              "age_range": [3,10]
            },
            {
              "school_type": "ms",
              "age_range": [11,13]
            }
          ],
          "workplace_size_counts_by_num_personnel": [
            [1,4,2947],
            [5,9,992]
          ]
        }"""
        return test_str

    def test_load_minimal_location(self):
        test_str = self.minimal_test_str()
        location = sp.load_location_from_json_str(test_str)

        self.assertEquals(len(location.data_provenance_notices), 2,
                          "Array length incorrect")

        self.assertEquals(location.data_provenance_notices[0], "notice1",
                          "Array entry incorrect")

        self.assertEquals(location.data_provenance_notices[1], "notice2",
                          "Array entry incorrect")

        self.assertEquals(len(location.reference_links), 2,
                          "Array length incorrect")

        self.assertEquals(location.reference_links[0], "reference1",
                          "Array entry incorrect")

        self.assertEquals(location.reference_links[1], "reference2",
                          "Array entry incorrect")

        self.assertEquals(len(location.citations), 2,
                          "Array length incorrect")

        self.assertEquals(location.citations[0], "citation1",
                          "Array entry incorrect")
        self.assertEquals(location.citations[1], "citation2",
                          "Array entry incorrect")

        self.assertEquals(len(location.population_age_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.population_age_distribution[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.population_age_distribution[0][0], 0,
                          "Array entry incorrect")
        self.assertEquals(location.population_age_distribution[0][1], 4,
                          "Array entry incorrect")
        self.assertEquals(location.population_age_distribution[0][2], 0.06,
                          "Array entry incorrect")

        self.assertEquals(len(location.population_age_distribution[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.population_age_distribution[1][0], 5,
                          "Array entry incorrect")
        self.assertEquals(location.population_age_distribution[1][1], 9,
                          "Array entry incorrect")
        self.assertEquals(location.population_age_distribution[1][2], 0.20,
                          "Array entry incorrect")

        self.assertEquals(len(location.employment_rates_by_age), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.employment_rates_by_age[0]), 2,
                          "Array length incorrect")
        self.assertEquals(location.employment_rates_by_age[0][0], 19,
                          "Array entry incorrect")
        self.assertEquals(location.employment_rates_by_age[0][1], 0.300,
                          "Array entry incorrect")

        self.assertEquals(len(location.employment_rates_by_age[1]), 2,
                          "Array length incorrect")
        self.assertEquals(location.employment_rates_by_age[1][0], 20,
                          "Array entry incorrect")
        self.assertEquals(location.employment_rates_by_age[1][1], 0.693,
                          "Array entry incorrect")

        self.assertEquals(len(location.enrollment_rates_by_age), 2,
                          "Array length incorrect")
        self.assertEquals(len(location.enrollment_rates_by_age[0]), 2,
                          "Array length incorrect")
        self.assertEquals(location.enrollment_rates_by_age[0][0], 2,
                          "Array entry incorrect")
        self.assertEquals(location.enrollment_rates_by_age[0][1], 0,
                          "Array entry incorrect")

        self.assertEquals(len(location.enrollment_rates_by_age[1]), 2,
                          "Array length incorrect")
        self.assertEquals(location.enrollment_rates_by_age[1][0], 3,
                          "Array entry incorrect")
        self.assertEquals(location.enrollment_rates_by_age[1][1], 0.529,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_head_age_brackets), 2,
                          "Array length incorrect")
        self.assertEquals(len(location.household_head_age_brackets[0]), 2,
                          "Array length incorrect")
        self.assertEquals(location.household_head_age_brackets[0][0], 18,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_brackets[0][1], 19,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_head_age_brackets[1]), 2,
                          "Array length incorrect")
        self.assertEquals(location.household_head_age_brackets[1][0], 20,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_brackets[1][1], 24,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_head_age_distribution_by_family_size), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.household_head_age_distribution_by_family_size[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[0][0], 2,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[0][1], 163,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[0][2], 999,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_head_age_distribution_by_family_size[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[1][0], 3,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[1][1], 115,
                          "Array entry incorrect")
        self.assertEquals(location.household_head_age_distribution_by_family_size[1][2], 757,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_size_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.household_size_distribution[0]), 2,
                          "Array length incorrect")
        self.assertEquals(location.household_size_distribution[0][0], 1,
                          "Array entry incorrect")
        self.assertEquals(location.household_size_distribution[0][1], 0.2781590909877753,
                          "Array entry incorrect")

        self.assertEquals(len(location.household_size_distribution[1]), 2,
                          "Array length incorrect")
        self.assertEquals(location.household_size_distribution[1][0], 2,
                          "Array entry incorrect")
        self.assertEquals(location.household_size_distribution[1][1], 0.3443313103056699,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_resident_to_staff_ratio_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.ltcf_resident_to_staff_ratio_distribution[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[0][0], 1,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[0][1], 1,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[0][2], 0.0,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_resident_to_staff_ratio_distribution[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[1][0], 2,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[1][1], 2,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_resident_to_staff_ratio_distribution[1][2], 5.0,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_num_residents_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.ltcf_num_residents_distribution[0]), 3,
                              "Array length incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[0][0], 0,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[0][1], 19,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[0][2], 0.0,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_num_residents_distribution[1]), 3,
                              "Array length incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[1][0], 20,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[1][1], 39,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_residents_distribution[1][2], 0.08955223880597014,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_num_staff_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.ltcf_num_staff_distribution[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[0][0], 0,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[0][1], 19,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[0][2], 0.014925373134328358,
                          "Array entry incorrect")

        self.assertEquals(len(location.ltcf_num_staff_distribution[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[1][0], 20,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[1][1], 39,
                          "Array entry incorrect")
        self.assertEquals(location.ltcf_num_staff_distribution[1][2], 0.07462686567164178,
                          "Array entry incorrect")

        self.assertEquals(len(location.school_size_distribution), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.school_size_distribution[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.school_size_distribution[0][0], 20,
                          "Array entry incorrect")
        self.assertEquals(location.school_size_distribution[0][1], 50,
                          "Array entry incorrect")
        self.assertEquals(location.school_size_distribution[0][2], 0.027522935779816515,
                          "Array entry incorrect")

        self.assertEquals(len(location.school_size_distribution[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.school_size_distribution[1][0], 51,
                          "Array entry incorrect")
        self.assertEquals(location.school_size_distribution[1][1], 100,
                          "Array entry incorrect")
        self.assertEquals(location.school_size_distribution[1][2], 0.009174311926605505,
                          "Array entry incorrect")

        self.assertEquals(len(location.school_types_by_age), 2,
                          "Array length incorrect")

        self.assertEquals(location.school_types_by_age[0].school_type, "pk-es",
                          "School type value incorrect")
        self.assertEquals(len(location.school_types_by_age[0].age_range), 2,
                          "Array length incorrect")
        self.assertEquals(location.school_types_by_age[0].age_range[0], 3,
                          "Array entry incorrect")
        self.assertEquals(location.school_types_by_age[0].age_range[1], 10,
                          "Array entry incorrect")

        self.assertEquals(location.school_types_by_age[1].school_type, "ms",
                          "School type value incorrect")
        self.assertEquals(len(location.school_types_by_age[1].age_range), 2,
                          "Array length incorrect")
        self.assertEquals(location.school_types_by_age[1].age_range[0], 11,
                          "Array entry incorrect")
        self.assertEquals(location.school_types_by_age[1].age_range[1], 13,
                          "Array entry incorrect")

        self.assertEquals(len(location.workplace_size_counts_by_num_personnel), 2,
                          "Array length incorrect")

        self.assertEquals(len(location.workplace_size_counts_by_num_personnel[0]), 3,
                          "Array length incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[0][0], 1,
                          "Array entry incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[0][1], 4,
                          "Array entry incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[0][2], 2947,
                          "Array entry incorrect")

        self.assertEquals(len(location.workplace_size_counts_by_num_personnel[1]), 3,
                          "Array length incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[1][0], 5,
                          "Array entry incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[1][1], 9,
                          "Array entry incorrect")
        self.assertEquals(location.workplace_size_counts_by_num_personnel[1][2], 992,
                          "Array entry incorrect")
