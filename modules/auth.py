from modules.user import get_user
import uuid


def login(username, password):
    user = get_user(username)
    if user.active == 0:
        raise UserInactive("Your user account is not active. Please talk with \
                           your admin")
    if not password == user.password:
        raise InvalidCredentials("Invalid credentials")
    token = uuid.uuid4()
    return user, token


# Exceptions

class UserInactive(Exception):
    pass


class InvalidCredentials(Exception):
    pass
