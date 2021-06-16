"""Simple API

This is a working example of a simple api done with
bottle.py and intended to be used as a Google Cloud Run
service.

"""

import bottle
import routes.auth
import routes.storage

app = bottle.Bottle()

app.mount("/auth", routes.auth.app)
app.mount("/storage", routes.storage.app)


@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
