"""
API endpoints for Flasky for users
"""
import unittest

from api_testing.api_framework.base_api import BaseApi
from api_testing.api_framework import utils


class UsersApi(BaseApi):
    """
    Class for Users api
    """
    def get_all_users_url(self):
        return self.base_url + '/api/users'

    def get_user_url(self, user=''):
        return self.base_url + '/api/users/' + user

    def get_token_url(self):
        return self.base_url + '/api/auth/token'

    def get_all_users(self):
        """ Get All Users """
        headers = utils.create_header()
        url = self.get_all_users_url()
        json_response = self.get(url, headers=headers)
        return {
            'url': url,
            'response': json_response['json_response']
        }

    def get_user(self, user='', token=None):
        headers = utils.create_header(token=token)
        url = self.get_user_url(user=user)
        json_response = self.get(url, headers=headers)
        return {
            'url': url,
            'response': json_response['json_response']
        }

    def update_user(self, user='', json={}, token=None):
        headers = utils.create_header(token=token)
        url = self.get_user_url(user=user)
        json_response = self.put(url, json, headers=headers)
        return {
            'url': url,
            'status_code': json_response['response'],
            'message': json_response['json_response']['message']
        }

    def get_token(self, auth_details=None):
        headers = utils.create_header(auth_details=auth_details)
        url = self.get_token_url()
        json_response = self.get(url, headers=headers)
        return {
            'url': url,
            'status_code': json_response['response'],
            'response': json_response['json_response']
        }


class Test_UsersApi(unittest.TestCase):

    def setUp(self):
        self.api = UsersApi()
        self.api.base_url = 'http://localhost:8080'

    def test_get_all_users(self):
        self.assertIsNotNone(self.api.get_all_users())

    def test_get_token_user(self):
        response= self.api.get_token(('alok', 'demo123'))
        self.assertIsNotNone(self.api.get_token(('alok', 'demo123')))

    def test_get_token_nouser(self):
        response = self.api.get_token()
        self.assertIsNotNone(self.api.get_token())
