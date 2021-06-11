from functools import wraps
from os import environ
from bottle import response, request


def enable_cors(_route_function):
    @wraps(_route_function)
    def _enable_cors(*args, **kwargs):
        http_origin = request.headers.get("ORIGIN", None)
        allowed_hosts = environ.get("CORS_DOMAINS", "").split(",")
        allowed_headers = [
            "Access-Control-Allow-Origin",
            "Authorization",
            "Content-Type"
        ]
        allowed_methods = "GET, POST, DELETE, PUT, OPTIONS"
        if http_origin in ["https://ekiim.xyz", *allowed_hosts]:
            response.headers["Access-Control-Allow-Origin"] = http_origin
            response.headers["Access-Control-Allow-Headers"] = ", ".join(
                allowed_headers + [h.lower() for h in allowed_headers]
            )
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Methods"] = allowed_methods
            response.status = 200

        if request.method == "OPTIONS":
            return {}
        return _route_function(*args, **kwargs)
    return _enable_cors
