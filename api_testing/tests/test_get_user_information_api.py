from api_testing.api_framework.api_interface import ApiInterface
from api_testing.tests.conftest import read_config_file

import pytest
import unittest
import allure


class TestGetUserInfo(unittest.TestCase):
    valid_credentials = None
    base_url = None
    token = None
    api = None

    @classmethod
    def setUpClass(cls):
        data = read_config_file()
        TestGetUserInfo.base_url = data['base_url']
        TestGetUserInfo.valid_credentials = data['valid_credentials']
        TestGetUserInfo.get_token()

    @classmethod
    def get_token(cls):
        TestGetUserInfo.api = ApiInterface(TestGetUserInfo.base_url)
        response = TestGetUserInfo.api.get_token(TestGetUserInfo.valid_credentials)
        assert response['status_code'] == 200
        assert response['response']['token'] is not None
        TestGetUserInfo.token = response['response']['token']
        print('get_token: ', TestGetUserInfo.token)

    @allure.step('Get User Information')
    @pytest.mark.run(order=1)
    def test_get_user_information(self):
        print('token: ', TestGetUserInfo.token)
        response = TestGetUserInfo.api.get_user(TestGetUserInfo.valid_credentials[0], TestGetUserInfo.token)
        print('test_get_user_information_1: ', response)
        self.assertEqual(response['response']['message'], 'retrieval succesful')
        self.assertIsNotNone(response['response']['payload'])

    @allure.step('Get User Information - No Token')
    @pytest.mark.run(order=1)
    def test_get_user_information_no_token(self):
        response = TestGetUserInfo.api.get_user(TestGetUserInfo.valid_credentials[0])
        print('test_get_user_information_2: ', response)
        self.assertEqual(response['response']['message'], 'Token authentication required')

    @allure.step('Get User Information - Right Token, Other User')
    @pytest.mark.run(order=1)
    def test_get_user_information_wrong_endpoint(self):
        response = TestGetUserInfo.api.get_user('testuser1001', TestGetUserInfo.token)
        print('test_get_user_information_3: ', response)
        self.assertEqual(response['response']['message'], 'retrieval succesful')