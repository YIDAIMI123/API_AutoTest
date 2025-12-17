import pytest
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil
from common.response_util import assert_base_response

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/message.yaml"))
def test_message(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]
    data = case_info["request"]["data"]
    
    response = RequestsUtil.send_request(method=method, url=url, params=params, data=data)

    json_r = assert_base_response(response,0,"success")

    # assert response.status_code == 200
    # assert json_r["code"] == 0
    # assert json_r["msg"] == "success"

    # print(response.text)