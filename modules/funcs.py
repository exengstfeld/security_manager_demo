# -*- coding: utf-8 -*-
from functools import wraps
from extensions import db
from models.user import Role


def verify_and_create_role(name):
    if not Role.query.filter_by(name=name).first():
        _role = Role(name)
        db.session.add(_role)
        db.session.commit()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function


def standard_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs), True
        except Exception as ex:
            # Parse the exception. Reqparse Validation exceptions comes with a
            # 'data' field containing the error messages
            _msg = getattr(ex, "data", str(ex))
            result = _msg, False
        return {
            "data": result[0],
            'success': result[1]
        }
    return wrapper
