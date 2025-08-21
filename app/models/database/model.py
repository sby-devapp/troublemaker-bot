# File: app/mdels/database/model.py

"""
Model (DBManager):

    - _insert() -> self
    - _update() -> self
    + save() -> self
    + get() -> self
    + delete() -> self
    + get_by_id(id: int) -> self
    + get_all() -> list[Model]
    + get_where(**kwargs) -> list[Model]
    + get_by_field(field: str, value: any) -> list[Model]

"""

from app.models.database.db_manager import DBManager


class Model:
    db_manager = DBManager()
    table_name = None

    def __init__(self, id: int = None):
        self.id = id
        if self.id is not None:
            self.get_by_id(self.id)

    def _insert(self):
        raise NotImplementedError("Subclasses must implement _insert method")

    def _update(self):
        raise NotImplementedError("Subclasses must implement _update method")

    def is_exists(self):
        if self.id is None:
            return False
        query = f"SELECT COUNT(*) FROM {self.table_name} WHERE id = ?"
        cursor = self.db_manager.execute(query, (self.id,))
        result = cursor.fetchone()  # fetch the first row
        return result and result[0] > 0

    def save(self):
        if self.is_exists():
            return self._update()
        else:
            return self._insert()

    def get(self):
        temp_id = self.id
        if not self.id:
            raise ValueError("ID must be set to get a record")
        query = f"""
        SELECT *
        FROM {self.table_name}
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id,))
        row = cursor.fetchone()
        self.load_object_from_row(row)
        self.id = temp_id
        cursor.close()
        return self

    def delete(self):
        if self.id is None:
            raise ValueError("ID must be set to delete a record")
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.db_manager.execute(query, (self.id,))
        self.id = None

    @classmethod
    def get_by_id(cls, id: int):
        return cls(id=id).get()

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.table_name}"
        results = cls.db_manager.execute(query)
        rows = []
        for row in results:
            obj = cls()
            obj.load_object_from_row(row)
            rows.append(obj)
        return rows

    @classmethod
    def get_where(cls, **kwargs):
        if not kwargs:
            return []
        conditions = " AND ".join(f"{key} = ?" for key in kwargs.keys())
        query = f"SELECT * FROM {cls.table_name} WHERE {conditions}"
        params = tuple(kwargs.values())
        results = cls.db_manager.execute(query, params)
        rows = []
        for row in results:
            obj = cls()
            obj.load_object_from_row(row)
            rows.append(obj)
        return rows

    @classmethod
    def get_by_field(cls, field: str, value: any):
        query = f"SELECT * FROM {cls.table_name} WHERE {field} = ?"
        results = cls.db_manager.execute(query, (value,))
        rows = []
        for row in results:
            obj = cls()
            obj.load_object_from_row(row)
            rows.append(obj)
        return rows

    def load_object_from_row(self, row):
        raise ValueError("Not imeplement it yet!")
