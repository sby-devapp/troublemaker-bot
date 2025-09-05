# File: app/models/chat.py
from .database.model import Model
import sqlite3
from datetime import datetime


class Chat(Model):
    table_name = "chats"

    def __init__(
        self,
        id=None,
        username=None,
        type=None,
        last_message_id=None,
        last_message_sent_at=None,
    ):
        self.id = id
        self.username = username
        self.type = type  # type of chat, e.g., 'private', 'group'
        self.last_message_id = last_message_id
        self.last_message_sent_at = last_message_sent_at

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id, username, last_message_id, last_message_sent_at)
        VALUES ( ?, ?, ?, ?)
        """
        params = (
            self.id,
            self.username,
            self.last_message_id,
            self.last_message_sent_at,
        )
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, params)
        self.id = cursor.lastrowid
        cursor.close()

        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET username = ?, last_message_id = ?, last_message_sent_at = ?
        WHERE id = ?
        """
        params = (
            self.username,
            self.last_message_id,
            self.last_message_sent_at,
            self.id,
        )
        self.db_manager.execute(query, params)
        return self

    def get_by_id(self, id):
        self.id = id
        return self.get()

    def get_by_username(self, username):
        query = f"SELECT * FROM {self.table_name} WHERE username = ?"
        result = self.db_manager.execute(query, (username,))
        if result:
            self.id, self.username, self.last_message_id, self.last_message_sent_at = (
                result[0]
            )
            return self
        else:
            raise ValueError(f"Chat with username {username} not found")

    def get_all(self):
        query = f"SELECT * FROM {self.table_name}"
        results = self.db_manager.execute(query)
        chats = []
        for row in results:
            chat = Chat(
                id=row[0],
                username=row[1],
                last_message_id=row[2],
                last_message_sent_at=row[3],
            )
            chats.append(chat)
        return chats

    def delete(self):
        if self.id is None:
            raise ValueError("ID must be set to delete a record")
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.db_manager.execute(query, (self.id,))
        self.id = None
        return self

    def save(self):
        if self.is_exists():
            return self._update()
        else:
            return self._insert()
