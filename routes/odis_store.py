import json
from json import dumps as json_dumps
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

app = BottleJson()

@app.get("/")
@app.post("/new")
def store_record(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501, "Error")

@app.post("/<serial_number>")
def update_record(*args, code = None, **kwargs):
    payload = bottle.request.json
    print(payload)
    raise bottle.HTTPError(501, "Error")

@app.get("/list")
def get_all_info(*args, **kwargs):
    payload = bottle.request.query.dict
    print(payload)
    raise bottle.HTTPError(501, "Error")

@app.get("/<serial_number>")
def get_serial_number(*args, **kwargs):
    payload = bottle.request.query.dict
    print(payload)
    raise bottle.HTTPError(501, "Error")
