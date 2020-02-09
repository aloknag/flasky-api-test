import json

from api_testing.api_framework.api_interface import ApiInterface
from api_testing.tests.conftest import read_config_file
from api_testing.tests.conftest import generate_fake_data
import pytest
import unittest
import allure


class TestAPIFlow(unittest.TestCase):

    @allure.step('Get User Token')
    def setUp(self):
        data = read_config_file()
        self.base_url = data['base_url']
        self.valid_credentials = data['valid_credentials']
        self.get_token()

    def get_token(self):
        self.api = ApiInterface(self.base_url)
        response = self.api.get_token(self.valid_credentials)
        self.token = response['response']['token']
        print('get_token: ', self.token)

    @allure.step('Fetch User Information')
    @pytest.mark.run(order=1)
    def test_get_user_information(self):
        self.user = self.valid_credentials[0]
        response = self.api.get_user(user=self.user, token=self.token)
        print('test_get_user_information: ', response)
        self.assertEqual(response['response']['message'], 'retrieval succesful')

    @allure.step('Get All Users')
    @pytest.mark.run(order=2)
    def test_get_all_users(self):
        response = self.api.get_all_users()
        print('test_get_all_users: ', response['response']['status'])
        self.assertEqual(response['response']['status'], 'SUCCESS')

    @allure.step('Update User Information')
    @pytest.mark.run(order=3)
    def test_update_user_information(self):
        self.user = self.valid_credentials[0]
        json_data = generate_fake_data()
        response = self.api.update_user(user=self.user, json=json.loads(json.dumps(json_data)), token=self.token)
        print('test_update_user_information: ', response)
        status_code = response['status_code']
        self.assertEqual(status_code, 201)

    @allure.step('Fetch Updated User Information')
    @pytest.mark.run(order=4)
    def test_get_updated_user_information(self):
        self.user = self.valid_credentials[0]
        response = self.api.get_user(user=self.user, token=self.token)
        print('test_get_updated_user_information: ', response)
        self.assertEqual(response['response']['message'], 'retrieval succesful')


if __name__ == '__main__':
    unittest.main()