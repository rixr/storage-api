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



@app.post("/asign/<license_number>/<device_serial>")
def assign_license(license_number=None, device_serial=None):
    raise bottle.HTTPError(501, "non")



@app.get("/list")
def get_all_license(*args, **kwargs):
    try:
        respuesta = get_storage_device()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)



@app.get("/device/<serial_number>")
def get_license_by_sn(*args, serial_number=None, **kwargs):
    if not serial_number:
        raise bottle.HTTPError(404, "Missing serial number")
    payload = bottle.request.json
    print(payload)
    try:
        date = str(payload['date'])
        # validación de fecha
        year, month, day = [int(x) for x in date.split("-")]
        print("Valid data")
    except:
        print("Invalid data")
        raise HTTPError(400)
    raise bottle.HTTPError(501, "Error")
