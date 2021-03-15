from pprint import pprint
import bottle

import routes.storage

app = bottle.Bottle()

app.mount("/storage", routes.storage.app)

@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
