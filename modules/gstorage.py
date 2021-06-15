from os import environ
from pathlib import Path
from io import BytesIO
from google.cloud import storage


def get_file_to_store(collection, filename):
    client = storage.Client()
    bucket = client.get_bucket(environ["GCLOUD_BUCKET"])
    target = str(Path(collection) / filename)
    blob = bucket.blob(target)
    if blob.exists():
        raise Exception("File already exists")
    return blob


def store_bytes(collection, filename, byte):
    target = get_file_to_store(collection, filename)
    target.upload_from_file(BytesIO(byte))


def store_string(collection, filename, text):
    target = get_file_to_store(collection, filename)
    target.upload_from_string(text)
