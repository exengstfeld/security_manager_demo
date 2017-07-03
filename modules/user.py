from models.user import User
from extensions import db


def create_user(user_data):
    username = user_data.get("username")
    if User.query.filter_by(username=username).first():
        raise UserAlreadyExists("User %s already exists" % username)
    user = User(user_data)
    db.session.add(user)
    db.session.commit()
    return user


def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise UserNotFound("User %s has not been found" % username)
    return user


def delete_user(username):
    user = get_user(username)
    user.active = 0
    db.session.commit()
    return user


def edit_user(username, user_data):
    user = get_user(username)
    for k, v in user_data.items():
        if v:
            setattr(user, k, v)
    db.session.commit()
    return user

# Exceptions


class UserNotFound(Exception):
    pass


class UserAlreadyExists(Exception):
    pass
