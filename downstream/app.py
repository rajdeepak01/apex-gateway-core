from flask import Flask, jsonify 
from shared.config import DOWNSTREAM_HOST, DOWNSTREAM_PORT, FLASK_DEBUG
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the Downstream API"
    }), 200

@app.route("/health", methods = ["GET"])
def health():
    return ({
        "status": "ok",
        "service": "downstream-api"
    }), 200

@app.route("/orders", methods = ["GET"])
def get_orders():
    return jsonify({
        "orders": [
            {
                "id": 1,
                "product" : "Laptop",
                "status" : "confirmed"
            },

            {
                "id" : 2,
                "product" : "Keyboard",
                "status" : "shipped"
            }
        ]
    }), 200

if __name__ == "__main__":
    app.run(
        host = DOWNSTREAM_HOST,
        port = DOWNSTREAM_PORT,
        debug = FLASK_DEBUG
    )