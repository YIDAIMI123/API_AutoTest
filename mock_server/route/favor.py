from flask import jsonify, request,Blueprint

favor_bp = Blueprint("favor",__name__)

@favor_bp.route("/api/user/fovar",methods=["POST"])
def mock_favor():
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