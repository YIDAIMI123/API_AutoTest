import pytest
import requests
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/ex.yaml"))
def test_login(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]
    data = case_info["request"]["data"]

    response = RequestsUtil.send_request(method=method, url=url, params=params, data=data)
    assert response.json()["code"] == 200
