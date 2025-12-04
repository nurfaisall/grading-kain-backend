from flask import Blueprint, jsonify, request
import services.init as init
import config.utils as utils

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
    result = {}
    result["total_sum"] = {}
    df = df.replace({np.nan: None})
    result["df"] = df.to_dict()
    for i in utils.list_yard:
        result["total_sum"][i] = df[i].sum()
    return jsonify(
        {
            "message": "Hello, World! This is a simple Flask app using Blueprints.",
            "status": "success",
            "data": result,
        }
    )   

main_bp.route("/gradingByMonth", methods=["GET"])
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
    result = {}
    result["total_sum"] = {}
    result["df"] = df.to_dict()
    for i in utils.list_yard:
        result["total_sum"][i] = df[i].sum()
    return jsonify(
        {
            "message": "Hello, World! This is a simple Flask app using Blueprints.",
            "status": "success",
            "data": result,
        }
    )   