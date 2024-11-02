from flask import Flask, Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
def hello_world():
    return render_template("index.html")

@routes.route("/test")
def test_route():
    return "<h1>Hello! This is a test route!</h1>"

@routes.route("/hello/<name>")
def say_hello(name=0):
    return f"<h1>Hello, {name}! It's nice to meet you!<h1>"
