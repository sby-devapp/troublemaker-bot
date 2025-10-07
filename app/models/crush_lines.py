from app.models.database.model import Model
import random


class CrushLine(Model):
    table_name = "crush_lines"

    def __init__(self, id=None):
        super().__init__(id)
        self.gender = None      # 'M', 'F', or None
        self.topic = None       # e.g., 'confession', 'stalking', 'dreams'
        self.content = None     # The actual gossip text with {user}
        self.used = 0           # Starts at 0, auto-incremented
        self.created_at = None  # Set by DB on insert
        self.update_at = None   # Set by DB on update

    def _insert(self):
        query = f"""
            INSERT INTO {self.table_name} (topic, gender, content)
            VALUES (?, ?, ?)
            RETURNING id, gender, topic, content, used, created_at, update_at;
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(
            query,
            (self.topic, self.gender, self.content)
        )
        row = cursor.fetchone()
        if row:
            self.load_object_from_row(row)
        return self

    def _update(self):
        """Update only non-None attributes (except id)."""
        fields = []
        values = []

        if self.topic is not None:
            fields.append("topic = ?")
            values.append(self.topic)
        if self.gender is not None:
            fields.append("gender = ?")
            values.append(self.gender)
        if self.content is not None:
            fields.append("content = ?")
            values.append(self.content)

        # Always update update_at if anything changes
        if fields:
            fields.append("update_at = CURRENT_TIMESTAMP")
            query = f"""
                UPDATE {self.table_name}
                SET {', '.join(fields)}
                WHERE id = ?
                RETURNING id, gender, topic, content, used, created_at, update_at;
            """
            values.append(self.id)
            cursor = self.db_manager.db.cursor()
            cursor.execute(query, values)
            row = cursor.fetchone()
            if row:
                self.load_object_from_row(row)
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.gender = row["gender"]
            self.topic = row["topic"]
            self.content = row["content"]
            self.used = row["used"] or 0
            self.created_at = row["created_at"] if row["created_at"] else None
            self.update_at = row["updated_at"] if row["updated_at"] else None

    @classmethod
    def get_random_crush_line(cls, user):
        """
        Get a random crush line from the 10 least-used lines (filtered by user gender),
        then increment its 'used' counter.
        """
        db = cls.db_manager.db
        cursor = db.cursor()

        if user.gender is None:
            select_query = f"""
                SELECT id, gender, topic, content, used, created_at, updated_at
                FROM {cls.table_name}
                ORDER BY used ASC, RANDOM()
                LIMIT 1
            """
            cursor.execute(select_query)
        else:
            select_query = f"""
                SELECT id, gender, topic, content, used, created_at, updated_at
                FROM {cls.table_name}
                WHERE gender = ?
                ORDER BY used ASC, RANDOM()
                LIMIT 1
            """
            cursor.execute(select_query, (user.gender,))

        row = cursor.fetchone()
        if row:
            crush_line = cls()
            crush_line.load_object_from_row(row)
            
            # Update the used counter
            update_query = f"UPDATE {cls.table_name} SET used = used + 1 WHERE id = ?"
            cursor.execute(update_query, (crush_line.id,))
            db.commit()
            
            return crush_line
        return None