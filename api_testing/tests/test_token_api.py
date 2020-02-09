from api_testing.api_framework.api_interface import ApiInterface
from api_testing.tests.conftest import read_config_file

import pytest
import unittest
import allure


class TestTokenApi(unittest.TestCase):

    @allure.step('Read Config for Data')
    def setUp(self):
        data = read_config_file()
        self.base_url = data['base_url']
        self.valid_credentials = data['valid_credentials']
        self.invalid_credentials = data['invalid_credentials']

    @allure.step('Token API With valid Credentials')
    @pytest.mark.run(order=1)
    def test_get_token_valid(self):
        self.api = ApiInterface(self.base_url)
        response = self.api.get_token(self.valid_credentials)
        assert response['status_code'] == 200
        assert response['response']['token'] is not None

    @allure.step('Token API with Invalid Credentials')
    @pytest.mark.run(order=2)
    def test_get_token_invalid(self):
        self.api = ApiInterface(self.base_url)
        response = self.api.get_token(self.invalid_credentials)
        print(response)
        self.assertEqual(response['status_code'], 401)
        self.assertEqual(response['response']['message'], 'Invalid User')

    @allure.step('Token API with NO Credentials')
    @pytest.mark.run(order=3)
    def test_get_token_no_header(self):
        self.api = ApiInterface(self.base_url)
        response = self.api.get_token()
        print(response)
        self.assertEqual(response['status_code'], 401)
        self.assertEqual(response['response']['message'], 'Invalid User')


if __name__ == '__main__':
    unittest.main()