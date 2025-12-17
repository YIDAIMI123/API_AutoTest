import pytest
import requests
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil
from common.response_util import assert_base_response

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/login.yaml"))
def test_login(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]
    data = case_info["request"]["data"]
    # headers = case_info["request"]["headers"]


    response = RequestsUtil.send_request(method=method,params=params,url=url,data=data)

    json_r = assert_base_response(response,0,"登录成功")

    # assert response.status_code == 200
    # json_r = response.json()
    # assert json_r["code"] == 0
    # assert json_r["msg"] == "登录成功"
    print(json_r)


    # datas = json_r["data"]
    # assert data["username"] == "qqqqqq"          # 登录账号

    print("Content-Type:", response.headers.get("Content-Type"))
    print("text:", response.text)
    print("json:", response.json())
    print("Headers:", response.headers)

