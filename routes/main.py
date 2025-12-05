from flask import Blueprint, jsonify, request
import numpy as np
import services.init as init
import config.utils as utils
import pandas as pd

main_bp = Blueprint("main", __name__)


@main_bp.route("/gradingByDay", methods=["GET"])
def gradingByDay():
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


@main_bp.route("/gradingByMonth", methods=["GET"])
def gradingByMonth():
    option = request.args.get("option")
    month = request.args.get("month")
    df = []

    for data in init.data:
        if data["name"] == option:
            df = data["data"]

    df["tahun_bulan"] = pd.to_datetime(df["TANGGAL"]).dt.strftime("%Y-%m")
    if month is None:
        month = df["tahun_bulan"].max()

    df = df[df["tahun_bulan"] == month]
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
