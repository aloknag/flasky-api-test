from api_testing.api_framework.api_interface import ApiInterface
from api_testing.tests.conftest import read_config_file

import pytest
import unittest
import allure


class TestGetAllUsers(unittest.TestCase):

    @allure.step('Read Config for Data')
    def setUp(self):
        data = read_config_file()
        self.base_url = data['base_url']

    @allure.step('Get All Users Information')
    @pytest.mark.run(order=1)
    def test_get_all_users(self):
        self.api = ApiInterface(self.base_url)
        response = self.api.get_all_users()
        print('test_get_all_users: ', response)
        assert response['response']['status'] == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()