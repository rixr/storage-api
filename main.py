import bottle

app = bottle.Bottle()

@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
