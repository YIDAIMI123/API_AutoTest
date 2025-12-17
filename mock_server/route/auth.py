from flask import jsonify, request,Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/user/login",methods=["POST"])
def mock_login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "123456":
        response = {
            "code": 0,
            "msg": "登录成功",
            "data": {
                "token": "fake-jwt-token"
            }
        }
    else:
        response = {
            "code": 1,
            "msg": "登录失败，用户名或密码错误",
            "data": ""
        }
    return jsonify(response)