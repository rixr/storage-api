import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.odis_store import *


app = BottleJson()


@app.post("/device/new")
def new_device(*args, **kwargs):
    payload = bottle.request.json
    obligatory_fields = ['brand', 'model', 'serial_number', 'date']
    try:
        if any(key not in payload for key in obligatory_fields):
            raise Exception()
        dt.date.fromisoformat(payload['date'])
        print("Datos validos")
        respuesta = store_new_device(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

@app.post("/license/new/<license_number>")
def new_license(license_number):
    try:
        license_file = bottle.request.files.get("license_file")
        payload = {
            "license_number": license_number,
            "license_file": license_file.file
        }
        print(license_file)
        respuesta = store_new_license(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

@app.post("/asign/<license_number>/<device_serial>")
def assign_license(license_number=None, device_serial=None):
    raise bottle.HTTPError(501, "non")


# EJEMPLO DE CURL PARA NUEVO REGISTRO
# curl "http://localhost:8080/new?brand=getac&model=vas6150c&serial_number=1234567&date=2000-11-22"


@app.post("/<serial_number>")
def update_record(*args, serial_number=None, **kwargs):
    if not serial_number:
        raise bottle.HTTPError(404, "Missing serial number")
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
