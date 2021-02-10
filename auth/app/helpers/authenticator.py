import jwt
import sys
sys.path.append("..")

from functools import wraps
from flask import request, jsonify, current_app
from models.models import User

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({
                "error": "Not authorized!"
            }), 403
        
        if not 'Bearer' in token:
            return jsonify({
                "error": "Invalid token"
            }), 403

        try:
            token_hash = token.replace("Bearer ", "")
            decoded_token = jwt.decode(
                token_hash,
                current_app.config['AUTH_SECRET_KEY'],
                algorithms="HS256"
            )
            current_user = User.query.get(decoded_token['id'])
        except:
            return jsonify({
                "error": "Invalid token!"
            })

        return f(*args, **kwargs)
    
    return wrapper
