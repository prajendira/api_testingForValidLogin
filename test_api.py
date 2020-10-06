import pytest
import requests
import json

#API test with post method
def main_url():
    return "https://reqres.in"

def test_valid_login():
    url = "https://reqres.in/api/login/"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    print(token)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"

"""
def test_valid_login(main_url):
    url = main_url + "/api/login"
    
"""