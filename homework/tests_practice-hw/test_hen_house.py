import unittest
from unittest.mock import patch
from lectures.tests.hen_house.hen_class import HenHouse, ErrorTimesOfYear

'''
To successfully Run this test module within 
systemwide Python3 environment from the root of 
the whole project you need to use following 
single-line command in terminal:
python -m homework.tests_practice-hw.test_hen_house
'''


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        # optional method, may be used to initialize hen_house instance
        self.hen_house = HenHouse(13)

    def test_a_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised
        with self.assertRaises(ValueError):
            HenHouse(2)

    def test_b_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as mocked:
            mocked.today().month = 12 or 1 or 2
            self.assertEqual(self.hen_house.season, "winter")

    def test_c_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as mocked:
            mocked.today().month = 3 or 4 or 5
            self.assertEqual(self.hen_house.season, "spring")

    def test_d_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as mocked:
            mocked.today().month = 6 or 7 or 8
            self.assertEqual(self.hen_house.season, "summer")

    def test_e_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as mocked:
            mocked.today().month = 9 or 10 or 11
            self.assertEqual(self.hen_house.season, "autumn")

    def test_f_productivity_index(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        with patch.object(HenHouse, 'season', "autumn"):
            self.assertEqual(0.5, self.hen_house._productivity_index())

    def test_g_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called
        with patch.object(HenHouse, 'season', "qwerty"):
            self.assertRaises(ErrorTimesOfYear,
                              lambda: self.hen_house._productivity_index())

    def test_h_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked
        pass

    def test_i_get_max_count_for_soup(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        pass

    def test_j_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        pass

    def test_k_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type
        pass

    def test_l_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
