from sqlalchemy import (
    create_engine,
    Table,
)
from flask_sqlalchemy import SQLAlchemy
import configparser


PERMISSION_ENGINE_PATH = "sqlite:///data.sqlite"


class SQLiteDB:
    ENGINE = create_engine(PERMISSION_ENGINE_PATH)
    DB = SQLAlchemy()
    CONFIG = configparser.ConfigParser()


class Users(SQLiteDB.DB.Model):
    id = SQLiteDB.DB.Column(SQLiteDB.DB.Integer, primary_key=True)
    username = SQLiteDB.DB.Column(SQLiteDB.DB.String(15), unique=True, nullable = False)
    email = SQLiteDB.DB.Column(SQLiteDB.DB.String(50), unique=True)
    password = SQLiteDB.DB.Column(SQLiteDB.DB.String(80))


PERMISSION_TABLE = Table(Users.__name__.lower(), Users.metadata)
