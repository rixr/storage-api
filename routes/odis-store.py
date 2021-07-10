from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle

app = bottle.Bottle()

@app.post("/new")
def store_record(*args, **kwargs):
    bottle.response.status_code = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Not implemented")

@app.post("/<serial_number>")
def update_record(*args, code = None, **kwargs):
    bottle.response.status_code = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/list")
def get_all_info(*args, **kwargs):
    bottle.response.status_code = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/<serial_number>")
def get_info_by_sn(*args, **kwargs):
    bottle.response.status_code = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")
    