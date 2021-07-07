from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle

STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.gstorage import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
else:
    raise Exception("Storage method not set")

app = bottle.Bottle()

@app.get("/new")
def store_record(*args, **kwargs):
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    return dict(code=200)


@app.get("/update")
def update_record(*args, **kwargs):
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    return dict(code=200)


@app.get("/info")
def all_info(*args, **kwargs):
    # data = bottle.request.json
    # filename = ""
    # store_string("dell", filename, json_dumps(data))
    return dict(code=200)


@app.get("/info/<code>")
def info_by_code(*args, code=None, **kwargs):
    pass
    return dict(code=200)
