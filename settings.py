import os


class BaseConfig(object):
    """ Base configuration for all deploy contexts """
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_HOST = "127.0.0.1"
    APP_PORT = 5500
    SECRET_KEY = "2622f44e-122e-4b14-b936-a7931f327e6f"

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/security_manager.db"

    STATIC_DIR = "/static"
    TEMPLATE_DIR = "/templates"


class DevelopmentConfig(BaseConfig):
    # Development configuration
    DEBUG = True


class ProductionConfig(BaseConfig):
    # Production configuration
    DEBUG = False
