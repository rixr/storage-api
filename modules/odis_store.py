import json
from modules.storage import (
    store_string,
    store_bytes,
    query_storage
)

# ESPECIFICO
def get_license_by_sn():
    pass

# TODAS
def get_storage_device(path=None):
    query_result = query_storage(
        "odis/device", #ruta en donde estan almacenadas las licencias
    )
    print(query_result)
    return query_result['content']



def store_new_device(brand=None, model=None, serial_number=None, date=None):
    filename = f"{brand}_{model}_{serial_number}.json"
    data = dict(brand=brand, model=model, serial_number=serial_number, date=date)
    store_string(
        "odis/device", # ruta en donde se almacenaran las licencias
        filename,
        json.dumps(data)
    )
    return f"odis/device/{filename}"

def store_new_license(license_number=None, license_file=None):
    filename = f"{license_number}_{date}.dat"
    store_bytes(
        "odis/license",
        filename,
        license_file.read()
    )
    return f"odis/device/{filename}"
