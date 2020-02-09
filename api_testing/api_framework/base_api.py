import requests
from urllib.error import HTTPError
from urllib.error import URLError


class BaseApi:
    """ Main Base API class
        Contains methods for GET, PUT, auth
    """
    def __init__(self):
        pass

    def get(self, url=None, headers={}):
        json_response = None
        error = {}
        try:
            response = requests.get(url=url, headers=headers)
            try:
                json_response = response.json()
            except Exception as e:
                print('put:', "Unable to get response.json")
                json_response = None
        except (HTTPError, URLError) as e:
            error = e
            print(e)
            raise e
        return {'response': response.status_code,
                'text': response.text,
                'json_response': json_response,
                'error': error}

    def put(self, url, json=None, headers={}):
        "Put request"
        error = {}
        response = False
        try:
            response = requests.put(url, json=json, headers=headers)
            try:
                json_response = response.json()
            except:
                print('put:', "Unable to get response.json")
                json_response = None
        except (HTTPError, URLError) as e:
            error = e
            print(e)
            raise e
        return {'response': response.status_code,
                'text': response.text,
                'json_response': json_response,
                'error': error}