import bottle

app = bottle.Bottle()

@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)
