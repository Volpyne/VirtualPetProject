import requests

from web.services import rest_api

def validate_credentials(user, password):
    body = {"username": user,
          "password": password}
    response = requests.post(f'{rest_api.API_URL}/login', json=body)

    return response.status_code == 200


def create_user(user, password, mail):
    body = {"username": user,
            "password": password,
            "mail": mail}
    response = requests.post(f'{rest_api.API_URL}/user', json=body)

    return response.status_code == 200


def obtain_users():
    response = requests.get(f'{rest_api.API_URL}/user')

    return response.json()

#diary


def create_diary(name):
    body = {"name": name}
    response = requests.post(f'{rest_api.API_URL}/diary', json=body)

    return response.status_code == 200


def obtain_diaries():
    response = requests.get(f'{rest_api.API_URL}/diary')

    return response.json()