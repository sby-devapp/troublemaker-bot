# File: app/models/database/db_manager.py

"""DBManager:
- db: SQLite3 database connection
+ connect()-> sqlite3.Connection
+ is_connected() -> bool
+ close() -> None
+ query(query: str, params: tuple = ()) -> query
+ execute()-> None
+ execute_sql_file(file_path: str) -> None


"""


class DBManager:
    db = None
    db_location = "database/db/"
    db_file_name = f"database"

    @classmethod
    def connect(cls, db_file_name=None):

        if db_file_name:
            import sqlite3

            cls.db_file_name = db_file_name
            db_path = cls.db_location + cls.db_file_name + ".db"
            cls.db = sqlite3.connect(db_path)
            cls.db.row_factory = sqlite3.Row
            print(f"Connecting to database at {db_path}")

        if cls.db is None:
            import sqlite3

            cls.db = sqlite3.connect(db_path)
            cls.db.row_factory = sqlite3.Row
            print(f"Connecting to database at {db_path}")
        return cls.db

    @classmethod
    def is_connected(cls):
        return cls.db is not None and cls.db.in_transaction

    @classmethod
    def close(cls):
        if cls.db is not None:
            cls.db.close()
            cls.db = None

    @classmethod
    def execute(cls, query: str, params: tuple = ()):
        if cls.is_connected() is False:
            cls.connect()
        cursor = cls.db.cursor()
        cursor.execute(query, params)
        cls.db.commit()
        # cls.close()
        return cursor

    @classmethod
    def execute_sql_file(cls, file_path: str):
        if cls.is_connected():
            cls.connect()
            raise Exception("Database connection is not established.")
        with open(file_path, "r", encoding="utf-8") as file:  # <-- add encoding
            sql_script = file.read()
        cursor = cls.db.cursor()
        cursor.executescript(sql_script)
        cls.db.commit()
        # cls.close()
        return cursor
