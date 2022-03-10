from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .constantes import CONFIG

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

db = SQLAlchemy()
login = LoginManager()

app = Flask(__name__,
    template_folder=templates,
    static_folder=statics)

from .routes import generic, api

def config_app(config_name="test"):
    app.config.from_object(CONFIG[config_name])
    db.init_app(app)
    login.init_app(app)
    return app