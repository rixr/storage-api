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
        print("Valid data")
        respuesta = store_new_device(**payload)
    except:
        print("Invalid data")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)



@app.post("/assign/<license_number>/<device_serial>")
def assign_license(license_number=None, device_serial=None):
    payload = bottle.request.json
    obligatory_fields = ['device_serial', 'license_number']
    try:
        if any(key not in payload for key in obligatory_fields):
            raise Exception("Invalid data")
        print("Valid data")
        respuesta = assign_license2device(**payload)
    except:
        print("Invalid data")
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
        print("Invalid data")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)



@app.get("/list")
def get_all_devices(*args, **kwargs):
    try:
        respuesta = get_storage_device()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)


@app.get("/device/<serial_number>")
def license_per_sn(*args, code=None, **kwargs):
    try:
        respuesta = get_license_by_sn(serial_number=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
