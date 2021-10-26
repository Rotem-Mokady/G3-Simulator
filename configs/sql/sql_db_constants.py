from app.utils.extractions import create_table_extraction


FLASK_DB_ATTR_NAME = "db"
TABLE_CREATION_QUERY_PATH = "configs/sql/auth_schema.sql"

BEGIN_CLOSE_DB_COMMAND_LINE = "delete db if exists..."
BEGIN_CREATION_COMMAND_LINE = "creating schema and table..."
FINISH_CREATION_COMMAND_LINE = "table created!"

AUTH_TABLE_NAME, AUTH_COLUMNS_NAMES = create_table_extraction(TABLE_CREATION_QUERY_PATH)

GET_DATA_FOR_USER_QUERY = f"SELECT * FROM {AUTH_TABLE_NAME} WHERE {AUTH_COLUMNS_NAMES[0]} = ?"
INSERT_DATA_FOR_USER_QUERY = f"""
INSERT INTO {AUTH_TABLE_NAME} {tuple(AUTH_COLUMNS_NAMES)} VALUES (?, ?, ?, ?)
"""

