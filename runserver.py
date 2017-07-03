# coding: utf-8
from app_factory import create_app
from extensions import db
from modules.funcs import verify_and_create_role

application = create_app()


with application.app_context():
    db.create_all()
    # If default roles are missing, we create them
    verify_and_create_role("admin")
    verify_and_create_role("worker")

if __name__ == '__main__':
    host = application.config["APP_HOST"]
    port = application.config["APP_PORT"]
    application.run(host=host, port=port)
