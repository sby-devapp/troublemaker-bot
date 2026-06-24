from app.models.database.model import Model


class BotIntervention(Model):
    table_name = "bot_interventions"

    def __init__(self, id=None):
        super().__init__(id)
        self.type = None
        self.content = None
        self.used = 0
        self.active = 1
        self.created_at = None

    def _insert(self):
        query = f"""
            INSERT INTO {self.table_name} (type, content, active)
            VALUES (?, ?, ?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.type, self.content, self.active))
        self.id = cursor.lastrowid
        cursor.close()
        return self

    def _update(self):
        query = f"""
            UPDATE {self.table_name}
            SET type = ?, content = ?, used = ?, active = ?
            WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.type, self.content, self.used, self.active, self.id))
        cursor.close()
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.type = row["type"]
            self.content = row["content"]
            self.used = row["used"] or 0
            self.active = row["active"] or 1
            self.created_at = row["created_at"]

    @classmethod
    def get_random_by_type(cls, intervention_type):
        """Get a random intervention of specified type, prioritizing least-used."""
        db = cls.db_manager.db
        cursor = db.cursor()

        query = f"""
            SELECT id, type, content, used, active, created_at
            FROM {cls.table_name}
            WHERE type = ? AND active = 1
            ORDER BY used ASC, RANDOM()
            LIMIT 1
        """
        cursor.execute(query, (intervention_type,))
        row = cursor.fetchone()

        if row:
            intervention = cls()
            intervention.load_object_from_row(row)
            
            # Increment used counter
            update_query = f"UPDATE {cls.table_name} SET used = used + 1 WHERE id = ?"
            cursor.execute(update_query, (intervention.id,))
            db.commit()
            
            return intervention
        return None
