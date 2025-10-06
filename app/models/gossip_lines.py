from app.models.database.model import Model
import random


class GossipLine(Model):
    """Model for handling gossip lines in the application."""

    table_name = "gossip_lines"

    def __init__(self, id=None, gender=None, content=None, used=0):
        self.id = id
        self.gender = gender
        self.content = content
        self.used = used

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
            # Support both dict-like and tuple rows
            if isinstance(row, dict):
                self.id = row["id"]
                self.gender = row["gender"]
                self.content = row["content"]
                self.used = row["used"]
            else:
                # Assume tuple in column order: id, gender, content, used
                self.id, self.gender, self.content, self.used = row

    @classmethod
    def get_random_gossip_line(cls, user):
        """
        Fetch a random gossip line from the 10 least-used lines (filtered by user gender if available),
        then increment its 'used' counter.
        Compatible with all SQLite versions (does NOT use RETURNING).
        """
        db = cls.db_manager.db
        db.execute("BEGIN IMMEDIATE")  # Acquire write lock early

        try:
            # Step 1: Get up to 10 least-used candidate IDs
            if user.gender is None:
                cursor = db.execute(f"""
                    SELECT id FROM {cls.table_name}
                    ORDER BY used ASC, RANDOM()
                    LIMIT 10
                """)
            else:
                cursor = db.execute(f"""
                    SELECT id FROM {cls.table_name}
                    WHERE gender = ?
                    ORDER BY used ASC, RANDOM()
                    LIMIT 10
                """, (user.gender,))

            candidate_ids = [row[0] for row in cursor.fetchall()]
            if not candidate_ids:
                db.rollback()
                return None

            # Step 2: Pick one at random
            chosen_id = random.choice(candidate_ids)

            # Step 3: Increment its 'used' count
            db.execute(f"""
                UPDATE {cls.table_name}
                SET used = used + 1
                WHERE id = ?
            """, (chosen_id,))

            # Step 4: Fetch the full updated row
            cursor = db.execute(f"""
                SELECT id, gender, content, used
                FROM {cls.table_name}
                WHERE id = ?
            """, (chosen_id,))
            row = cursor.fetchone()

            db.commit()

            if row:
                gossip_line = cls()
                gossip_line.load_object_from_row(row)
                return gossip_line
            return None

        except Exception:
            db.rollback()
            raise