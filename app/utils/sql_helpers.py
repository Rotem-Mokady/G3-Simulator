import os
from flask import (
    current_app,
    g,
)
import sqlite3
import re

# local modules
from configs.sql import sql_db_constants
from configs import secrets


def open_sql_schema(db_name: str) -> sqlite3.Connection:
    """
    create local SQLite DB
    """
    if sql_db_constants.FLASK_DB_ATTR_NAME not in g:
        g.db = sqlite3.connect(
            db_name, detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_sql_schema() -> None:
    """
    close SQLite DB connection
    :return:
    """
    db = g.pop(sql_db_constants.FLASK_DB_ATTR_NAME, None)

    if db is not None:
        db.close()


def create_table_in_schema(path: str = sql_db_constants.TABLE_CREATION_QUERY_PATH) -> None:
    """
    create schema in exists SQLite db
    """
    if not os.path.exists(path):
        raise ValueError(f"Path '{path}' does not exist")
    db = open_sql_schema(db_name=secrets.AUTH_DB_NAME)

    current_app.root_path = os.getcwd()
    with current_app.open_resource(path) as f:
        try:
            db.executescript(f.read().decode("utf-8"))
        except sqlite3.OperationalError as err:
            if re.match(re.compile(r"table\s\w+\salready exists"), err.__str__()):
                pass




