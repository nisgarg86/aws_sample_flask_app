"""
factory method to create main flask application
"""

from flask import Flask

from app.health.controller import health_module


def create_app():
    """
    creates and returns main flask application
    :return:
    """

    app = Flask(__name__)  # todo: what does this statement do - sets the name of the flask app module

    with app.app_context():
        app.register_blueprint(health_module)

    return app



