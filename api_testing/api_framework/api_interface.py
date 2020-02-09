"""
A composed interface for all the API objects
Use the API_Player to talk to this class
"""
from api_testing.api_framework.users_api import UsersApi


class ApiInterface(UsersApi):
    """
    A composed interface for the API objects
    """

    def __init__(self, url):
        super().__init__()
        self.base_url = url
