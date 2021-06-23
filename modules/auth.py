from functools import wraps
from os import environ
from bottle import response, request
import jwt


def validate_token(token):
    data = jwt.decode(token, environ["APP_SECRET"], algorithms=["HS256"])
    print(data)
    return True


def auth_required(_route_function):
    @wraps(_route_function)
    def _auth_required(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        # Bearer <token>
        validity = validate_token(auth_header.split(" ")[-1])
        if not auth_header or not validity:
            response.status = 403
            return {}
        return _route_function(*args, **kwargs)
    return _auth_required
