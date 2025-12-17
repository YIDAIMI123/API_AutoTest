import pytest
import requests

def assert_base_response(response,code,msg=None):
    assert response.status_code == 200
    json_r = response.json()
    assert json_r["code"] == code
    if msg:
        assert json_r["msg"] == msg
    return json_r