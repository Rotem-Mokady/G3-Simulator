import os
from flask_login import (
    LoginManager,
    UserMixin,
)

from configs.secrets.db_constants import (
    PERMISSION_ENGINE_PATH,
    Users,
)


SERVER_CONFIG = {
    "SECRET_KEY": os.urandom(12),
    "SQLALCHEMY_DATABASE_URI": PERMISSION_ENGINE_PATH,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
}


LOGIN_MANAGER = LoginManager()


class UsersApp(UserMixin, Users):
    pass
