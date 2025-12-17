import pytest
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil
from common.response_util import assert_base_response

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/search.yaml"))
def test_search(case_info):
    method = case_info["request_search"]["method"]
    url = case_info["request_search"]["url"]
    params = case_info["request_search"]["params"]
    data = case_info["request_search"]["data"]
    # headers = case_info["request"]["headers"]

    response = RequestsUtil.send_request(method=method, url=url, params=params, data=data)
    print(response.status_code, response.text[:200])
    print(response.url)

    json_r = assert_base_response(response,0,"success")

    # assert response.status_code == 200
    # assert json_r["code"] == 0
    # assert json_r["msg"] == "success"

