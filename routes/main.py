from flask import Blueprint, jsonify
import services.init as init

main_bp = Blueprint('main', __name__)

@main_bp.route('/main')
def hello_world():
    data = init .data[0]['data'].to_dict()
    return jsonify({
        "message": "Hello, World! This is a simple Flask app using Blueprints.",
        "status": "success",
        "data": data
    })
