import os
from app.models.database.db_manager import DBManager


def menu():

    menu_text = """
    0)  Delete Database.
    1)  Create Database schema.
    2)  Execute SQL File.
    3)  Exit.
    """
    print(menu_text)
    i = input("Choose a number between 1-3: ")
    try:
        i = int(i)

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return True

    try:
        if i == 0:
            if os.path.exists(DBManager.db_file_name):
                DBManager.close()
                os.remove(DBManager.db_file_name)
                print(f"Database '{DBManager.db_file_name}' deleted successfully.")
            else:
                print(f"Database '{DBManager.db_file_name}' does not exist.")
        elif i == 1:
            DBManager.connect()
            DBManager.execute_sql_file("database/sql/schema.sql")
        elif i == 2:
            DBManager.connect()
            file_name = input("Write the file name (e.g., filename.sql): ")
            # remove all spaces from file_name
            file_name = file_name.replace(" ", "")
            file_path = f"database/sql/{file_name}"
            if not file_path.endswith("sql"):
                file_path = f"{file_path}.sql"
            if os.path.exists(file_path):
                print(f"[Execute]: {file_path} ")
                DBManager.execute_sql_file(file_path)
                print(f"[Execute]: {file_path} is executed with success")
            else:
                print(f"File '{file_path}' does not exist.")
            DBManager.close()
        elif i == 3:
            return False
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return True


if __name__ == "__main__":
    # i want to use it like this > python init.py [database_file]
    import sys

    db_file = sys.argv[1] if len(sys.argv) > 1 else DBManager.db_file_name
    # Ensure db_file is in the format "database/{db_name}.db"
    if not db_file.startswith("database/db/"):
        db_file = f"database/db/{db_file}"
    if not db_file.endswith(".db"):
        db_file = f"{db_file}.db"
    DBManager.connect(db_file)
    while menu():
        pass
    DBManager.close()
