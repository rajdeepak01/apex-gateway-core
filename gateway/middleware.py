from flask import request, g
import uuid

def log_request():
	request_id = request.headers.get("X-Request-ID")

	if not request_id:
		request_id = str(uuid.uuid4())

	g.request_id = request_id

	print(f"Incoming request: {request.method} {request.path}")

def log_response(response):
	response.headers["X-Request-ID"] = g.request_id
	print(
		f"Outgoing response: "
		f"{response.status_code} "
		f"request_id={g.request_id}"
	)

	return response

