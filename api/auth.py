# coding: utf-8
from flask_restful import Resource, reqparse
from modules.funcs import standard_response
from modules.auth import login


class AuthResource(Resource):
    method_decorators = [standard_response]

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("username", required=True,
                            help="Need username field")
        parser.add_argument("password", required=True,
                            help="Need password field")
        args = parser.parse_args()
        data, token = login(args["username"], args["password"])
        return {"user": data.as_dict(), "token": str(token)}
