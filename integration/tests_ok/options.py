from app import app


@app.route("/options/hello")
def options_hello():
    return "Hello!"
