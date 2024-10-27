from flask import Flask, Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@routes.route("/test")
def test():
    return "<p>Hello, Test!</p>"
