# File: app/models/user.py
from app.models.database.model import Model


class User(Model):
    table_name = "users"

    def __init__(self, id=None, username=None, first_name=None, last_name=None):
        super().__init__()
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id, username, first_name, last_name) VALUES (?, ?, ?, ?)
        """
        values = (self.id, self.username, self.first_name, self.last_name)
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, values)
        self.id = cursor.lastrowid
        cursor.close()
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET username = ?, first_name = ?, last_name = ?
        WHERE id = ?
        """
        values = (self.username, self.first_name, self.last_name, self.id)
        self.db_manager.execute(query, values)
        return self

    def full_name(self):
        full_name = ""
        if self.first_name:
            full_name = self.first_name
        if self.last_name:
            full_name = f"{full_name} {self.last_name}"
        if full_name == " ":
            full_name = f"@{self.username}"
        return full_name

    def load_from_row(self, row):
        if not row:
            return None
        self.id = row[0]
        self.username = row[1]
        self.first_name = row[2]
        self.last_name = row[3]

    def get_random_user_except(self, user_id: int):
        """
        Get a random user except the given user_id.
        """
        if user_id is None:
            raise ValueError("user_id must be provided")
        query = f"""
        SELECT *
        FROM {self.table_name}
        WHERE id != ?
        ORDER BY RANDOM()
        LIMIT 1
        """
        cursor = self.db_manager.execute(query, (user_id,))
        row = cursor.fetchone()
        if row:
            self.load_from_row(row)
            return self
        return None
