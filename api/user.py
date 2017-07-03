# coding: utf-8
from flask_restful import Resource, reqparse
from modules.user import create_user, get_user, edit_user, delete_user
from modules.funcs import standard_response


class UserResource(Resource):
    method_decorators = [standard_response]

    def get(self, username=None):
        data = get_user(username)
        return data.as_dict()

    def delete(self, username=None):
        delete_user(username)
        data = get_user(username)
        return data.as_dict()

    def post(self, username=None):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("username", required=True,
                            help="Need username field")
        parser.add_argument("password", required=True,
                            help="Need password field")
        parser.add_argument("name", required=True,
                            help="Need name field")
        parser.add_argument("email", required=True,
                            help="Need email field")
        parser.add_argument("role_id", required=True,
                            help="Need role_id field")
        args = parser.parse_args()
        data = create_user(args)
        return data.as_dict()

    def put(self, username=None):
        parser = reqparse.RequestParser()
        parser.add_argument("password")
        parser.add_argument("name")
        parser.add_argument("email")
        parser.add_argument("role_id")
        args = parser.parse_args()
        data = edit_user(username, args)
        return data.as_dict()
