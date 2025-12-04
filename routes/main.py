from flask import Blueprint, jsonify, request
import services.init as init

main_bp = Blueprint("main", __name__)


@main_bp.route("/gradingByDay", methods=["GET"])
def hello_world():
    option = request.args.get("option")
    day = request.args.get("day")
    df = []

    for data in init.data:
        if data["name"] == option:
            df = data["data"]

    if day is None:
        day = df["TANGGAL"].max()

    df = df[df["TANGGAL"] == day]
    grade

    result = {}
    df = df.to_dict()
    return jsonify(
        {
            "message": "Hello, World! This is a simple Flask app using Blueprints.",
            "status": "success",
            "data": {"df": df},
        }
    )
