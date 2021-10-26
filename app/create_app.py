import os
from flask import Flask
from oauthlib.oauth2 import WebApplicationClient

from configs import secrets
from configs.dash import settings
from app.user_auth import add_login_manager
from app.utils.sql_helpers import create_table_in_schema
from app.routes import add_index, add_dash, add_login, add_callback


def create_app() -> Flask:
    app: Flask = Flask(__name__,
                       template_folder=settings.TEMPLATES_FOLDER_PATH,
                       static_folder=settings.STATIC_FOLDER_PATH)
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
    add_login_manager(app)
    add_dash(app)
    with app.app_context():
        create_table_in_schema()
    client = WebApplicationClient(secrets.GOOGLE_CLIENT_ID)

    add_index(app)
    add_login(app, client)
    add_callback(app, client)

    return app

