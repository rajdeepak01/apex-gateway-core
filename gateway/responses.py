from flask import g, jsonify


def success_response(data, status_code=200):
    return jsonify({
        "request_id": g.get("request_id"),
        "data": data
    }), status_code