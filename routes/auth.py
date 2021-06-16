import bottle


app = bottle.Bottle()


@app.get("/")
def root_index(*args, **kwargs):
    print("I'm in auth")
    return dict(code=200)


def validate_user(user, password):
    return len(password) > 8


@app.route("/login", method=["POST", "OPTIONS"])
def auth_login(*args, **kwargs):
    payload = bottle.request.json
    if not payload:
        raise Exception("Not valid data")
    print(payload)
    user = payload.get("username", None)
    password = payload.get("password", None)
    if user and password and validate_user(user, password):
        bottle.response.status = 200
        bottle.response.content_type = "application/json"
        return dict(code=200, token="auth-token")
    bottle.response.status = 401
    bottle.response.content_type = "application/json"
    return dict(code=401)
