import pytest
from threading import Thread
import time
import requests
from flask import jsonify
# @pytest.fixture(scope="session")
# def mock_token():
#     # 启动 mock Flask server 在后台线程
#     def run_server():
#         app.run(debug=False, use_reloader=False, port=5000) #之所以运行app.run()服务器会一直运行（需要ctrl+c终止），是因为它以阻塞的方式开启服务器，所以这里需要用线程执行，否则后面的代码不会执行
#                                                             #而且app.run()这一步是开启服务器，不是执行里面的函数
#     server_thread = Thread(target=run_server)
#     server_thread.daemon = True  # 测试结束时自动关闭
#     server_thread.start()
    
#     # 等待 Mockserver 启动（1-2 秒）
#     time.sleep(2)
    
#     # 从 mock 登录获取虚拟 token
#     response = requests.post(
#         "http://127.0.0.1:5000/api/user/login",
#         json={"username": "admin", "password": "123456"},
#         headers={"Content-Type": "application/json"}
#     )
    
#     if response.status_code == 200:
#         token = response.json()["data"]["token"]
#         yield token  # 返回 token 给测试用例
#     else:
#         raise Exception("Mock login failed")
    
    # 无需手动关闭，daemon=True 会自动处理

# @pytest.fixture(scope="session")
# def mock_favor():
#     def run_server():
#         app.run(debug=False, use_reloader=False, port=5000)

#     server_thread_1 = Thread(target=run_server)
#     server_thread_1.daemon = True
#     server_thread_1.start()
#     # 等待 Mockserver 启动（1-2 秒）
#     time.sleep(2)

#     response = requests.post(
#         url="http://127.0.0.1:5000/api/fovar",
#         json={"token": "fake-jwt-token"},
#         headers={"Content-Type": "application/json"}
#     ) 
#     if response.status_code == 200:
#         favor = response.json()
#         yield favor
#     else:
#         raise Exception("Mock favor failed")
    

# @pytest.fixture(scope="session")
# def mock_delete_browse():
#     def run_server():
#         app.run(debug=False, use_reloader=False, port=5000)

#     server_thread_2 = Thread(target=run_server)
#     server_thread_2.daemon = True
#     server_thread_2.start()

#     time.sleep(2)

#     response = requests.post(
#         url="http://127.0.0.1:5000/api/usergoodsbrowse_delete/index",
#         json={"token": "fake-jwt-token"},
#         headers={
#             "Content-Type": "application/json"
#         }
#     )
#     if response.status_code == 200:
#         delete_browse = response.json()
#         yield delete_browse
#     else:
#         Exception("Mock delete browse failed")

@pytest.fixture(scope="session")
def mock_server_url():
    return "http://127.0.0.1:5000"

@pytest.fixture(scope="session")
def mock_token(mock_server_url):
    response = requests.post(
        url=f"{mock_server_url}/api/user/login",
        json={
            "username": "admin",
            "password": "123456"
        },
        headers={"Content-Type": "application/json"}
    )
    return response.json()["data"]["token"]
