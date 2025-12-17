import pytest
import requests

def test_login_mock():
    response = requests.request(
        method="POST",
        url = "http://127.0.0.1:5000/api/user/login",
        json={
            "username": "admin",
            "password": "123456"
        },
        headers={
            "Content-Type": "application/json"
        }
    )
    print(response.status_code)
    print(response.json())