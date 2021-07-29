import json
import os
import bottle
from json import dumps as json_dumps
from time import time
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.odis_store import *

app = BottleJson()

@app.get("/")
@app.post("/new")
def new(*args, **kwargs):
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    try:
        brand = str(payload['brand'])
        model = str(payload['model'])
        serial_number = int(payload['serial_number'])
        # Archivo
        file = get_storage_file(payload['license'])
        date = str(payload['date'])
        # validación de fecha
        year, month, day = [int(x) for x in date.split("-")]
        print("Datos validos")
        respuesta = store_register(**payload)
        # validación de extension de archivo
    except:
        print("Datos invalidos")
        raise HTTPError(400)
    raise bottle.HTTPError(501, "Error")
# EJEMPLO DE CURL PARA NUEVO REGISTRO
# curl "http://localhost:8080/new?brand=getac&model=vas6150c&serial_number=1234567&date=2000-11-22"

@app.post("/<serial_number>")
def update_record(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        date = str(payload['date'])
        # validación de fecha
        year, month, day = [int(x) for x in date.split("-")]
        print("Datos validos")
    except:
        print("Datos invalidos")
        raise HTTPError(400)
    raise bottle.HTTPError(501, "Error")

# EJEMPLO DE CURL PARA ACTUALIZAR REGISTRO
# curl "http://localhost:8080/1234567?date=2000-11-22"

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
