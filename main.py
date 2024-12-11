from flask import Flask

app = Flask(__name__)

API = "Eom1c6+gnvHYgqriJ59jxw==82P94Rxfh2JiHHQW"
@app.route("/")
def main():
    return "<h1>this page home page</h1>"

@app.route("/about")
def about():
    return "<h1>This page about page</h1>"

@app.route("/add/<int:a>/<int:b>")
def user(a, b):
    return f"<h1>Natija:{a + b}</h1>"

if __name__ == "__main__":
    app.run(debug=True)