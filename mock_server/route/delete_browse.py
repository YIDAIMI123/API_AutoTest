from flask import jsonify, request, Blueprint

delete_browse_bp = Blueprint("delete_browse", __name__)

@delete_browse_bp.route("/api/user/usergoodsbrowse_delete/index", methods=["POST"])
def mock_delete_browse():
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
    return jsonify(response)