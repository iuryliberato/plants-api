# save this as app.py
from flask import Flask

from flask_bcrypt import Bcrypt

# ! import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# ! Import the uri
from config.environment import db_URI

from flask_marshmallow import Marshmallow

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


# ! Added this configuration
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

# ! Instatiate the SQLAlchemy class
db = SQLAlchemy(app)

mash = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import plants, users

app.register_blueprint(plants.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")
