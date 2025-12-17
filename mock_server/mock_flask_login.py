from flask import Flask, jsonify, request

#创建一个应用对象
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "为什么进不去"

@app.route("/api/user/login", methods=["POST"])
def login():
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

@app.route("/api/fovar",methods=["POST"])
def favor():
    token = request.json.get("token")
    if token == "fake-jwt-token":
        response = {
            "code": 0,
            "msg": "收藏成功",
            "data": ""
        }
    else:
        response = {
            "code": 1,
            "msg": "收藏失败,token无效",
            "data": ""
        }
    return jsonify(response)

@app.route("/api/usergoodsbrowse_delete/index",methods=["POST"])
def delete_browse():
    token = request.json.get("token")
    if token == "fake-jwt-token":
        response = {
            "code": 0,
            "msg": "删除成功",
            "data": ""
        }
    else:
        response = {
            "code": 1,
            "msg": "删除失败,token无效",
            "data": ""
        }
    return jsonify(response) #josonify 把字典转换为 JSON 格式的响应

if __name__ == "__main__":
    app.run(debug=True)