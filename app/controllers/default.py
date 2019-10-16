from app import app


@app.route("/")
def index():
    return "Hello World PÁE!"
