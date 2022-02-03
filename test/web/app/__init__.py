from logging import StreamHandler
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from flask.logging import default_handler


loggingFormat = '[%(asctime)s] : [%(levelname)s] : %(message)s'
# logging.basicConfig(filename='logger.log', format=loggingFormat, level=logging.DEBUG)
formatter = logging.Formatter(loggingFormat)

app = Flask(__name__)

handler = StreamHandler()
handler.setFormatter(formatter)

app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.logger.removeHandler(default_handler)

flask_env = os.environ.get('FLASK_ENV', None)

CORS(app)

app.config.from_object("app.config.Config")

db = SQLAlchemy(app)

api = Api(app)


# ROUTES
@app.route("/health")
def hello_world():
    return jsonify(hello="server up")

@app.teardown_appcontext
def shutdown_session(exception=None):
    print("closing session on request end")
    db.session.remove()

from app.routes import create_routes

create_routes(api)
