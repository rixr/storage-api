import json
from os import environ
from pathlib import Path
from modules.storage import *

def store_register(brand=None, model=None, serial_number=None, date=None):
    print("From module ./routes/odis_store")
    print(brand, model, serial_number, date)
    return "Success"

def get_license_to_store(collection, filename):
    target = str(Path(collection) / filename)
    blob = get_blob(target)
    if blob.exists():
        raise Exception("License already exists")
    return blob

def get_storage_license(path=""):
    target = (storage_dir / path)
    if not target.exists() or not target.is_file():
        raise Exception("Does not exists")
    mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
    return mime, target.read_bytes()

def store_string(collection, filename, text):
    target = get_license_to_store(collection, filename)
    target.upload_from_string(text)
