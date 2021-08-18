import os
import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.odis_store import *

# Ruta predeterminada
app = BottleJson()

@app.post("/device/new")
def new_device(*args, **kwargs):
    """
    Ruta para agregar un nuevo equipo de diagnóstico
    """
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



@app.post("/assign/<license_number>/<serial_number>")
def assign_license(license_number, serial_number):
    """
    Ruta para asinar una licencia a un equipo de diagnóstico
    """
    try:
        respuesta = assign_license2device()
    except:
        print("Invalid data")
        raise bottle.HTTPError(400, "MALA RESPUESTA")
    raise bottle.HTTPError(201, respuesta)



@app.post("/license/new/<license_number>")
def new_license(license_number):
    """
    Ruta para agregar una nueva licencia
    """
    try:
        license_file = bottle.request.files.get("license_file")
        license_size = os.stat(license_file).st_size()
        print(license_size)
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
    """
    Ruta para consultar todos los equipos registrados
    """
    try:
        respuesta = get_storage_device()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)


@app.get("/device/<serial_number>")
def license_per_sn(*args, code=None, **kwargs):
    """
    Ruta para consultar equipos registrados dado su numero de serie
    """
    try:
        respuesta = get_license_by_sn(serial_number=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
