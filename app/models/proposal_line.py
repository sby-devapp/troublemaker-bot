from app.models.database.model import Model


class ProposalLines(Model):
    """Model for handling propositions in the application."""

    table_name = "proposal_lines"

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
    def get_random_proposal_line(cls, user):
        """Get a random proposition based on the user's gender."""
        if user.gender is None:
            query = f"""
                SELECT * FROM {cls.table_name}
                WHERE gender IS NULL
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
        # print(f"user: id: {user.id}, name: {user.full_name()}, gender: {user.gender}")
        # print(f"sql Proposal line query: {query}")
        # print(f"sql Proposal line row: {row}")
        if row:
            proposal_line = cls()
            proposal_line.load_object_from_row(row)
            return proposal_line
        return None
