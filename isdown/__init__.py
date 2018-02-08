from os import environ

from flask import Flask

from .blueprints import register_blueprints
from .models import db, create_all


def create_app():
    app = Flask(__name__)

    app = load_config(app)

    register_error_handlers(app)
    initialize_extensions(app)
    register_blueprints(app)

    return app


def load_config(app):
    # template directories
    app.template_folder = "_templates"
    app.static_folder = "_static"

    # environment variable
    envvar_name = 'FLASK_APP_ENVIRONMENT'
    env = environ.get(envvar_name, None)
    if env is None:
        default = "Production"
        print(
            "{var} is not specified, using {default} config.".format(
                var=envvar_name,
                default=default
            )
        )
        exit(1) if not default else None

    try:
        import config
        app.config.from_object(
            "config.{var}".format(var=env)
        )
    except ImportError as ie:
        print("ImportError: Cannot import config\n")
        raise ie

    return app


def register_error_handlers(app):
    """ registers error handlers (404, Exception, etc) """
    if app.config.get('ERRORHANDLING_INTERNAL', False):
        with app.app_context():
            pass


def initialize_extensions(app):
    # init database
    db.init_app(app)
    with app.app_context():
        create_all()
