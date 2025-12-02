from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/main')
def hello_world():
    return jsonify({
        "message": "Hello, World! This is a simple Flask app using Blueprints.",
        "status": "success"
    })
