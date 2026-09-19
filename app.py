from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {name}!"

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

