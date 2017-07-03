# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from extensions import db
from settings import DevelopmentConfig
from api import bp_api


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_error_handlers(app)
    built_extensions(app)
    register_blueprints(app)
    return app


def built_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(bp_api, url_prefix="/api")


def register_error_handlers(app):

    @app.errorhandler(404)
    def render_error(error):
        return jsonify({"data": "Unkown service!", "success": False}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"data": "We're sorry :(", "success": False}), 500
