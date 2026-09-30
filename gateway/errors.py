from flask import g, jsonify
from werkzeug.exceptions import HTTPException

def handle_http_error(error):
    response = {
        "request_id": g.get("request_id"),
        "error": {
            "code": error.name.upper().replace(" ", "_"),
            "message": error.description
        }
    }

    return jsonify(response), error.code

def handle_unexpected_error(error):
    response = {
        "request_id" : g.get("request_id"),
        "error" : {
            "code" : "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred. Please try again later."
        }
    }

    return jsonify(response), 500

def register_error_handlers(app):
    app.register_error_handler(HTTPException, handle_http_error)
    app.register_error_handler(Exception, handle_unexpected_error)