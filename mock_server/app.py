from flask import Flask, jsonify, request
from route.auth import auth_bp
from route.favor import favor_bp
from route.delete_browse import delete_browse_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(favor_bp)
    app.register_blueprint(delete_browse_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)