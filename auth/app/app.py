import os

from flask import Flask
from models.models import db, configure
from routes.routes import blue_print

app = Flask(__name__)
db_config_host = os.getenv('DB_HOST')
db_config_user = os.getenv('DB_USER')
db_config_pass = os.getenv('DB_PASS')
app_secret_key = os.getenv('AUTH_SECRET_KEY')
app.config['AUTH_SECRET_KEY'] = app_secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqlconnector://{db_config_user}:{db_config_pass}@{db_config_host}/author'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

configure(app)
app.register_blueprint(blue_print)

with app.app_context():
    db.create_all()
