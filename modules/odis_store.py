import json
from modules.storage import store_string, store_bytes


def get_license_to_store():
    pass

def get_storage_license(path=None):
    pass

def store_new_device(brand=None, model=None, serial_number=None, date=None):
    filename = f"{brand}_{model}_{serial_number}.json"
    data = dict(brand=brand, model=model, serial_number=serial_number, date=date)
    store_string(
        "odis/device",
        filename,
        json.dumps(data)
    )
    return f"odis/device/{filename}"

def store_new_license(license_number=None, license_file=None):
    filename = f"{license_number}.cert"
    store_bytes(
        "odis/license",
        filename,
        license_file.read()
    )
    return f"odis/device/{filename}"

