from app.models.database.model import Model


class Action(Model):
    table_name = "actions"

    def __init__(self, id=None, action_name=None):
        self.id = id
        self.action_name = action_name

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id, action_name)
        VALUES (?, ?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id, self.action_name))
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET action_name = ?
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.action_name, self.id))
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.action_name = row["action_name"]
        else:
            raise ValueError("Row data is empty or invalid")

    def get_random_proposition(self, user):
        from app.models.proposition import Proposition

        return Proposition.get_random_proposition_from_action(self, user)
