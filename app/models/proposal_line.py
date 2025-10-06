from app.models.database.model import Model
import random


class ProposalLines(Model):
    """Model for handling propositions in the application."""

    table_name = "proposal_lines"

    def __init__(self, id=None, gender=None, content=None, used=0):
        self.id = id
        self.gender = gender
        self.content = content
        self.used = used if used is not None else 0

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
            # Support both dict and tuple (though your current code assumes dict)
            if isinstance(row, dict):
                self.id = row["id"]
                self.gender = row["gender"]
                self.content = row["content"]
                self.used = row["used"]
            else:
                self.id, self.gender, self.content, self.used = row

    @classmethod
    def get_random_proposal_line(cls, user):
        """
        Fetch a random proposal line from the 10 least-used lines (filtered by user gender),
        then increment its 'used' counter.
        Compatible with all SQLite versions.
        """
        db = cls.db_manager.db
        db.execute("BEGIN IMMEDIATE")

        try:
            # Step 1: Fetch up to 10 least-used candidate IDs
            if user.gender is None:
                cursor = db.execute(f"""
                    SELECT id FROM {cls.table_name}
                    WHERE gender IS NULL
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
                # Fallback: try opposite logic if no matches (optional)
                # For now, just return None
                db.rollback()
                return None

            # Step 2: Pick one at random
            chosen_id = random.choice(candidate_ids)

            # Step 3: Increment 'used'
            db.execute(f"""
                UPDATE {cls.table_name}
                SET used = used + 1
                WHERE id = ?
            """, (chosen_id,))

            # Step 4: Fetch full updated row
            cursor = db.execute(f"""
                SELECT id, gender, content, used
                FROM {cls.table_name}
                WHERE id = ?
            """, (chosen_id,))
            row = cursor.fetchone()

            db.commit()

            if row:
                proposal_line = cls()
                proposal_line.load_object_from_row(row)
                return proposal_line
            return None

        except Exception:
            db.rollback()
            raise

    # Optional: You can now safely remove `increase_used()` if unused,
    # since incrementing is handled inside `get_random_proposal_line`.