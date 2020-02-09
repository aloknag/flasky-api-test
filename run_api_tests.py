import json

import requests
from requests.auth import HTTPBasicAuth

user = 'alok'
password = 'demo123'

response = requests.get('http://localhost:8080/api/auth/token', auth=HTTPBasicAuth(user, password))
print(response.json())
token = response.json()['token']


def put_value(user, data):
    headers = {'Content-Type': 'application/json', 'token': token}
    json_data = json.loads(json.dumps(data))
    response = requests.put("http://localhost:8080/api/users/" + user, json=json_data, headers=headers)
    print(response.json())


def get_value(user):
    headers = {'Content-Type': 'application/json', 'token': token}
    json_data = json.loads(json.dumps(data))
    response = requests.get("http://localhost:8080/api/users/" + user, headers=headers)
    print(response.json())


user = 'alok'
data = {'firstname': "Alok", "field": "value"}
put_value(user, data)
get_value(user)
user = "' or 1==1;"
# put_value(user, data)  ## Bug here.
user = "'' or 1=1;"
# get_value(user)   ## Bug Here