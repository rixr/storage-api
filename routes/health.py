import bottle

app = bottle.Bottle()


@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)


@app.post("/print")
@app.post("/print/")
@app.post("/print/<name>")
@app.post("/print/<name>/")
@app.post("/print/<name>/<matricula>")
def post_print(*args, name="Mike", matricula="007"):
    kwargs = dict(name=name, matricula=matricula)
    print("Calling print endpoint")
    print(args, kwargs, sep="\t")
    return dict(code=201, py=dict(args=args, kwargs=kwargs))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
