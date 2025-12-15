import pytest
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil

@pytest.mark.parametrize("case_info",YamlUtil.read_yaml_testcase("./data/ex.yaml"))
def test_login(case_info):
    method = case_info["request"]["method"]
    url = case_info["request"]["url"]
    params = case_info["request"]["params"]
    data = case_info["request"]["data"]


    response = RequestsUtil.send_request(method=method,params=params,url=url,json=data)
    assert response.status_code == 200
    json_r = response.json()
    assert json_r["code"] == 0
    assert json_r["msg"] == "登录成功"
    assert "data" in json_r
    assert "token" in json_r["data"]
    assert json_r["data"]["token"] != ""

    # datas = json_r["data"]
    # assert data["username"] == "qqqqqq"          # 登录账号
   
    print("输出前")
    print(json_r["data"])
    print("输出后") 