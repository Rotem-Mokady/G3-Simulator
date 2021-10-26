from flask import Flask
from flask_login import (
    UserMixin,
    LoginManager,
)
from typing import Union

# local modules
from app.utils.sql_helpers import (
    open_sql_schema,
)
from app.utils.extractions import create_table_extraction
from configs.sql import sql_db_constants
from configs import secrets


class User(UserMixin):
    def __init__(self, **kwargs) -> None:

        self.table_params_check(**kwargs)

        self.id = kwargs["user_id"]
        self.name = kwargs["user_name"]
        self.email = kwargs["email"]
        self.profile_pic = kwargs["profile_pic"]

    @staticmethod
    def table_params_check(**kwargs) -> None:
        table_params = create_table_extraction(sql_db_constants.TABLE_CREATION_QUERY_PATH)
        if not table_params:
            raise TypeError("probably not a create table query")
        columns = table_params[1]
        if list(kwargs.keys()) != columns:
            raise KeyError(f"no match between input and table params ({', '.join(columns)})")

    @staticmethod
    def get(user_id: str) -> Union[UserMixin, None]:
        db = open_sql_schema(db_name=secrets.AUTH_DB_NAME)
        user = db.execute(
            sql_db_constants.GET_DATA_FOR_USER_QUERY, (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            user_id=user[0], user_name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(**kwargs) -> None:
        User.table_params_check(**kwargs)
        db = open_sql_schema(db_name=secrets.AUTH_DB_NAME)
        db.execute(
            sql_db_constants.INSERT_DATA_FOR_USER_QUERY,
            tuple(kwargs.values()),
        )
        db.commit()


def add_login_manager(app: Flask) -> None:

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
