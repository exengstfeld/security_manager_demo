from flask import Blueprint
from api.user import UserResource
from api.auth import AuthResource
from flask_restful import Api

bp_api = Blueprint('api', __name__)

api = Api(bp_api)

api.add_resource(UserResource, '/user/<string:username>', "/user")
api.add_resource(AuthResource, '/login')
