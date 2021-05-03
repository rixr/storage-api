from os import environ
from datetime import datetime
from json import dumps as json_dumps
from pathlib import Path

import bottle
from google.cloud import storage

from modules.cors import enable_cors

app = bottle.Bottle()

@app.route("/form", method=["POST", "OPTIONS"])
@enable_cors
def route_form(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return {}


@app.route("/file", method=["POST", "OPTIONS"])
@enable_cors
def route_file(*args, **kwargs):
    form_file = bottle.request.files.get("file")
    upload, object_path = store_object("files", form_file.filename, form_file.file)
    bottle.response.status = upload and 201 or 500
    bottle.response.content_type = "application/json"
    return dict(upload=upload, ref=object_path)


@app.route("/json", method=["POST", "OPTIONS"])
@enable_cors
def route_json(*args, **kwargs):
    payload=bottle.request.json
    obj = dict(
        record_name=payload.get("record_name", "unnamed"),
        namespace=payload.get("namespace", "no_namespace"),
        formname=payload.get("formname", None),
        prefix=payload.get("prefix", None),
        path=payload.get("path", None),
        datetime=get_timestamp(),
        payload=payload
    )
    namespace = obj.get("namespace")
    record_name = obj.get("record_name")
    upload, object_path = store_object(
        f"json/{namespace}",
        f"{record_name}.json",
        json_dumps(obj))
    bottle.response.status = upload and 201 or 500
    bottle.response.content_type = "application/json"
    return dict(upload=upload, ref=object_path)


def get_json_source(data):
    data.get("formname", data.get("source", {}).get(""))


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")


def timestamp_filename(filename):
    timestamp = get_timestamp()
    return "_".join([timestamp, filename])


def storage_blob(collection, filename):
    client = storage.Client()
    bucket = client.get_bucket(environ["GCLOUD_BUCKET"])
    file = Path(filename)
    object_path = str(
        Path(collection) / file.parent / timestamp_filename(file.name)
    )
    return bucket.blob(object_path), object_path


def store_object(collection, filename, data):
    returnable = False, None
    try:
        blob, object_path = storage_blob(collection, filename)
        if isinstance(data, str):
            blob.upload_from_string(data)
        else:
            blob.upload_from_file(data)
        returnable = True, object_path
    except Exception as e:
        print(e)
    return returnable
