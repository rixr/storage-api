import json
from json import dumps as json_dumps
from time import time
import bottle
from modules.bottles import BottleJson

app = BottleJson()

@app.get("/")
def store_record(*args, **kwargs):
    return dict(code= 201, message = "ok")

@app.post("/new")
def store_record(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    return dict(code= 201, message = "ok")

@app.post("/<serial_number>")
def update_record(*args, code = None, **kwargs):
    payload = bottle.request.json
    print(payload)
    return dict(code= 201, message = "ok")

@app.get("/list")
def get_all_info(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    return dict(code= 201, message = "ok")

@app.get("/<serial_number>")
def get_info_by_sn(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    return dict(code= 201, message = "ok")
