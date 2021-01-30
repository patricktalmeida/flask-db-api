import time
import os

from app.routes.routes import blue_print
from app.models.models import db, configure
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    db_config_host = os.getenv('DB_HOST')
    app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqlconnector://root:root@{db_config_host}/author'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    configure(app)
    app.register_blueprint(blue_print)
    
    with app.app_context():
        db.create_all()

    return app
