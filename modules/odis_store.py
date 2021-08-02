import datetime as dt
import json
import re
from modules.storage import (
    store_string,
    store_bytes,
    query_storage
)

def assign_license2device(license_number=None, serial_number=None):
    filename = f"{serial_number}_{license_number}.json"
    data = dict(license_number=license_number, serial_number=serial_number)
    store_string(
        "odis/assign",
        filename,
        json.dumps(data)
    )
    return f"odis/assign/{filename}"



def store_new_device(brand=None, model=None, serial_number=None, date=None):
    filename = f"{brand}_{model}_{serial_number}.json"
    data = dict(brand=brand, model=model, serial_number=serial_number, date=date)
    store_string(
        "odis/device", # ruta en donde se almacenaran los equipos
        filename,
        json.dumps(data)
    )
    return f"odis/device/{filename}"



def store_new_license(license_number=None, license_file=None):
    date = dt.date.today().isoformat()
    filename = f"{license_number}_{date}.dat"
    store_bytes(
        "odis/license", # ruta en donde se almacenaran las licencias
        filename,
        license_file.read()
    )
    return f"odis/license/{filename}"



# TODO
def get_storage_device(path=None):
    query_result = query_storage(
        "odis/device", #ruta en donde estan almacenadas los equipos
    )
    print(query_result)
    return query_result['content']



# ESPECIFICO
def get_license_by_sn(serial_number=None):
    query_result = query_storage(
        "odis/license", # ruta donde se almacenan las licencias
    )
    if serial_number is None:
        return query_result["content"]
    if serial_number is not None:
        return [
            r
            for r in query_result["content"]
            if serial_number in r
        ]
