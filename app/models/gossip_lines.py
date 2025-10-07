from app.models.database.model import Model
import random


class GossipLine(Model):
    """Model for handling gossip lines with timestamps."""

    table_name = "gossip_lines"

    def __init__(self, id=None):
        self.id = id
        self.gender = None
        self.topic = None
        self.content = None
        self.used = None
        self.created_at = None
        self.updated_at = None

    def _insert(self):
        # ✅ INSERT with auto-timestamps (SQLite sets created_at/updated_at)
        query = f"""
        INSERT INTO {self.table_name}
        (gender, topic, content)
        VALUES (?, ?, ?)
        """
        values = (self.gender, self.topic, self.content)
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, values)
        self.id = cursor.lastrowid
        
        # Fetch the full row (including auto-filled timestamps)
        cursor.execute(f"""
            SELECT id, gender, topic, content, used, created_at, updated_at
            FROM {self.table_name}
            WHERE id = ?
        """, (self.id,))
        row = cursor.fetchone()
        if row:
            self.load_object_from_row(row)
        return self

    def _update(self):
        # ✅ UPDATE + auto-update updated_at
        query = f"""
        UPDATE {self.table_name}
        SET
            gender = ?,
            topic = ?,
            content = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(
            query,
            (self.gender, self.topic, self.content, self.id)
        )
        
        # Reload the updated row
        cursor.execute(f"""
            SELECT id, gender, topic, content, used, created_at, updated_at
            FROM {self.table_name}
            WHERE id = ?
        """, (self.id,))
        row = cursor.fetchone()
        if row:
            self.load_object_from_row(row)
        return self

    def load_object_from_row(self, row):
        if not row:
            return
        if isinstance(row, dict):
            self.id = row["id"]
            self.gender = row["gender"]
            self.topic = row["topic"]
            self.content = row["content"]
            self.used = row["used"]
            self.created_at = row["created_at"]
            self.updated_at = row["updated_at"]
        else:
            # Tuple order MUST match SELECT order
            (
                self.id,
                self.gender,
                self.topic,
                self.content,
                self.used,
                self.created_at,
                self.updated_at
            ) = row

    @classmethod
    def get_random_gossip_line(cls, user):
        """
        Fetch a random gossip line from the 10 least-used lines (filtered by user gender),
        increment 'used', and return the full row with timestamps.
        Compatible with all SQLite versions.
        """
        db = cls.db_manager.db
        db.execute("BEGIN IMMEDIATE")

        try:
            # Step 1: Get candidate IDs
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

            # Step 2: Pick one
            chosen_id = random.choice(candidate_ids)

            # Step 3: Increment 'used' (updated_at auto-updates via trigger or DEFAULT)
            db.execute(f"""
                UPDATE {cls.table_name}
                SET used = used + 1, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (chosen_id,))

            # Step 4: Fetch full row with timestamps
            cursor = db.execute(f"""
                SELECT id, gender, topic, content, used, created_at, updated_at
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