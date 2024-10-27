from flask import Flask
from routes import routes

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(routes)
    app.run(host="0.0.0.0", port=8080)
