import pytest
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/index.yaml"))
def test_index(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]

    response = RequestsUtil.send_request(method=method, url=url, params=params)
    json_r = response.json()

    assert response.status_code == 200
    assert json_r["code"] == 0
    assert json_r["msg"] == "success"

    # print(response.text)
