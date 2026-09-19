from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

