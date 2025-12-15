import pytest
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/region.yaml"))
def test_region(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]
    data = case_info["request"]["data"]


    response = RequestsUtil.send_request(method=method, params=params, url=url, data=data)
    assert response.status_code == 200
    json_r = response.json()
    assert json_r["code"] == 0
    assert json_r["msg"] == "success"

    # print(response.text)
