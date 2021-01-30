from flask import current_app
from jwt import PyJWT as jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from app.classes.exeptions import DBDownException
from app.schemas.schemas import UserSchema
from app.models.models import User, db
from app.helpers.authenticator import jwt_required

blue_print = Blueprint('app', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@blue_print.route("/auth/healthcheck")
def healthcheck():
    is_db_up = True

    try:
        db.session.execute('SELECT 1')
    except:
        is_db_up = False
        raise DBDownException
    return 'API is ready to recieve connections!', 200

@blue_print.route("/auth/register", methods=['POST'])
def register_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    user = User(
        username,
        email,
        password
    )

    db.session.add(user)
    db.session.commit()

    result = user_schema.dump(
        User.query.filter_by(email=email).first()
    )

    return jsonify(result), 201

@blue_print.route("/auth/login", methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first_or_404()

    if not user.verify_password(password):
        return jsonify({
            "error": "Incorrect password"
        }), 403

    payload = {
        "id": user.id,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }

    token = jwt.encode(
        self=None,
        payload=payload,
        key=current_app.config['AUTH_SECRET_KEY']
    )

    return jsonify({"token": token}), 200

@blue_print.route("/auth/protected")
@jwt_required
def protected_example_route():
    result = users_schema.dump(
        User.query.all()
    )

    return jsonify(result)
