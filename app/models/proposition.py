from app.models.database.model import Model


class Proposition(Model):
    table_name = "propositions"

    def __init__(self, id=None, action_id=None, proposition=None):
        self.id = id
        self.action_id = action_id
        self.proposition = proposition

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id, action_id, proposition)
        VALUES (?, ?, ?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id, self.action_id, self.proposition))
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET action_id = ?, proposition = ?
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.action_id, self.proposition, self.id))
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.action_id = row["action_id"]
            self.proposition = row["proposition"]
        else:
            raise ValueError("Row data is empty or invalid")

    @classmethod
    def get_random_proposition_from_action(cls, action, user):
        if user.gender in ["male", "female"]:
            query = f"""
            SELECT * FROM {cls.table_name}
            WHERE action_id = ? and gender = ?
            ORDER BY RANDOM()
            LIMIT 1
            """
            cursor = cls.db_manager.db.cursor()
            cursor.execute(query, (action.id, user.gender))
            row = cursor.fetchone()
        else:
            query = f"""
            SELECT * FROM {cls.table_name}
            WHERE action_id = ?
            ORDER BY RANDOM()
            LIMIT 1
            """
            cursor = cls.db_manager.db.cursor()
            cursor.execute(query, (action.id,))
            row = cursor.fetchone()
        if row:
            proposition = Proposition()
            proposition.load_object_from_row(row)
            return proposition
        else:
            return None
