import json
import os
from faker import Faker


def read_config_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/config.json') as f:
        data = json.load(f)
    return data


def generate_fake_data():
    """ return fake user details as JSON """
    fake = Faker()
    firstname = fake.first_name()
    familyname = fake.last_name()
    phone_number = fake.phone_number()
    data = {'firstname': firstname,
            'lastname': familyname,
            'phone': phone_number
            }
    return data