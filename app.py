import omniifer_api
import omniinfer_account
import atexit
import logging
from flask import Flask, request, jsonify

import config

omniifer_api.api_key(config.api_key)
omniinfer_account.DEFAULT_CREDIT(config.default_credit)
omniinfer_account.UPDATE_INTERVAL(config.update_interval)
system = omniinfer_account.system("./data/")


def exit_():
    global system
    system.stopping()


atexit.register(exit_)

app = Flask(__name__)


@app.before_request
def auth_verify():
    auth_key = request.headers.get("Omni-System-Key")
    if auth_key != config.auth_key:
        logging.warning("Http: Unauthorized")
        return jsonify({"code": 1, "msg": "Unauthorized"}), 401


@app.route("/api/create_account", methods=['POST'])
def create_account():
    logging.info("Http: create_account")
    try:
        global system
        data = request.get_json()
        return jsonify(system.create_account(data["account_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/add_task", methods=['POST'])
def add_task():
    logging.info("Http: add_task")
    try:
        global system
        data = request.get_json()
        return jsonify(system.add_task(data["account_id"], data["mode"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/get_result", methods=['POST'])
def get_result():
    logging.info("Http: get_result")
    try:
        global system
        data = request.get_json()
        return jsonify(system.get_result(data["account_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/set", methods=['POST'])
def set_():
    logging.info("Http: set")
    try:
        global system
        data = request.get_json()
        return jsonify(system.set(data["account_id"], data["mode"], data["key"], data["value"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/set_person_api_key", methods=['POST'])
def set_person_api_key():
    logging.info("Http: set_person_api_key")
    try:
        global system
        data = request.get_json()
        return jsonify(system.set_person_api_key(data["account_id"], data["api_key"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/get", methods=['POST'])
def get():
    logging.info("Http: get")
    try:
        global system
        data = request.get_json()
        return jsonify(system.get(data["account_id"], data["mode"], data["key"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/put_model", methods=['POST'])
def put_model():
    logging.info("Http: put_model")
    try:
        global system
        data = request.get_json()
        return jsonify(system.put_model(data["model_version_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/search_model", methods=['POST'])
def search_model():
    logging.info("Http: search_model")
    try:
        global system
        data = request.get_json()
        return jsonify(system.search_model(data["keyword"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/model_enable", methods=['POST'])
def model_enable():
    logging.info("Http: model_enable")
    try:
        global system
        data = request.get_json()
        return jsonify(system.model_enable(data["model_version_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/get_info", methods=['POST'])
def get_info():
    logging.info("Http: get_info")
    try:
        global system
        data = request.get_json()
        return jsonify(system.get_info(data["account_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/set_model_name_by_version_id", methods=['POST'])
def set_model_name_by_version_id():
    logging.info("Http: set_model_name_by_version_id")
    try:
        global system
        data = request.get_json()
        return jsonify(system.set_model_name_by_version_id(data["account_id"], data["mode"], data["version_id"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/set_credit", methods=['POST'])
def set_credit():
    logging.info("Http: set_credit")
    try:
        global system
        data = request.get_json()
        return jsonify(system.set_credit(data["account_id"], data["credit"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/add_credit", methods=['POST'])
def add_credit():
    logging.info("Http: add_credit")
    try:
        global system
        data = request.get_json()
        return jsonify(system.add_credit(data["account_id"], data["credit"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/add_prompt", methods=['POST'])
def add_prompt():
    logging.info("Http: add_prompt")
    try:
        global system
        data = request.get_json()
        return jsonify(system.add_prompt(data["account_id"], data["mode"], data["prompt"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/api/add_negative_prompt", methods=['POST'])
def add_negative_prompt():
    logging.info("Http: add_negative_prompt")
    try:
        global system
        data = request.get_json()
        return jsonify(system.add_negative_prompt(data["account_id"], data["mode"], data["prompt"]))
    except KeyError:
        return jsonify({"code": 1, "msg": "Parameter Error"})


@app.route("/")
def main_page():
    return """
    <html><body>
    <a>omni infer api</a>
    </body></html>
    """
