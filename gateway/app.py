from flask import Flask

from gateway.errors import register_error_handlers
from gateway.middleware import log_request, log_response
from gateway.responses import success_response
from shared.config import GATEWAY_HOST, GATEWAY_PORT, FLASK_DEBUG

app = Flask(__name__)

register_error_handlers(app)

app.before_request(log_request)
app.after_request(log_response)


@app.route("/health", methods=["GET"])
def health():
    return success_response({
        "status": "ok",
        "service": "gateway"
    })


@app.route("/", methods=["GET"])
def home():
    return success_response({
        "message": "API Reliability Platform Gateway"
    })


if __name__ == "__main__":
    app.run(
        host=GATEWAY_HOST,
        port=GATEWAY_PORT,
        debug=FLASK_DEBUG
    )