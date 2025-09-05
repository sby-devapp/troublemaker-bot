from app.models.database.model import Model


class GossipLine(Model):
    """Model for handling gossip lines in the application."""

    table_name = "gossip_lines"

    def __init__(self, id=None, gender=None, content=None):
        self.id = id
        self.gender = gender
        self.content = content

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name}
        (gender, content)
        VALUES (?, ?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.gender, self.content))
        self.id = cursor.lastrowid
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET
            gender = ?, content = ?
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.gender, self.content, self.id))
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.gender = row["gender"]
            self.content = row["content"]

    @classmethod
    def get_random_gossip_line(cls, user):
        """Get a random gossip line based on the user's gender."""
        if user.gender is None:
            query = f"""
                SELECT * FROM {cls.table_name}
                ORDER BY RANDOM()
                LIMIT 1
            """
            cursor = cls.db_manager.db.cursor()
            cursor.execute(query)
        else:
            query = f"""
                SELECT * FROM {cls.table_name}
                WHERE gender = ?
                ORDER BY RANDOM()
                LIMIT 1
            """
            cursor = cls.db_manager.db.cursor()
            cursor.execute(query, (user.gender,))
        row = cursor.fetchone()
        if row:
            gossip_line = cls()
            gossip_line.load_object_from_row(row)
            return gossip_line
        return None
