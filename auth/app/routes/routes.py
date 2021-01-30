import datetime

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.classes.exeptions import DBDownException
from app.schemas.schemas import UserSchema
from app.models.models import User, db

blue_print = Blueprint('app', __name__)
user_schema = UserSchema()

@blue_print.route("/auth/healthcheck")
def healthcheck():
    is_db_up = True

    try:
        db.session.execute('SELECT 1')
    except:
        is_db_up = False
        raise DBDownException
    return 'API is ready to recieve connections!', 200

# @blue_print.route("/auth/register", methods=['POST'])
# def register_user():
#     return jsonify({"teste": "ok"}), 200
@blue_print.route("/auth/register", methods=['POST'])
def register_user():
    pass

@blue_print.route("/auth/login", methods=['POST'])
def login_user():
    pass