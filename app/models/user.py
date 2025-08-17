# File: app/models/user.py
import random
from app.models.database.model import Model


class User(Model):
    table_name = "users"

    def __init__(
        self,
        id=None,
        username=None,
        first_name=None,
        last_name=None,
        age=99,
        gender=None,
    ):
        super().__init__()
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id, username, first_name, last_name, gender, age) VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (
            self.id,
            self.username,
            self.first_name,
            self.last_name,
            self.gender,
            self.age,
        )
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, values)
        cursor.close()
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET username = ?, first_name = ?, last_name = ?, gender = ?, age = ?
        WHERE id = ?
        """
        values = (
            self.username,
            self.first_name,
            self.last_name,
            self.gender,
            self.age,
            self.id,
        )
        self.db_manager.execute(query, values)
        return self

    def full_name(self):
        full_name = ""
        if self.first_name:
            full_name = self.first_name
        if self.last_name:
            full_name = f"{full_name} {self.last_name}"
        if full_name == " ":
            full_name = f"@{self.username}"
        return full_name

    def load_object_from_row(self, row):

        if not row:
            return None
        self.id = row["id"]
        self.username = row["username"]
        self.first_name = row["first_name"]
        self.last_name = row["last_name"]
        self.age = row["age"] if "age" in row else 99
        self.gender = row["gender"]

    def am_in_group(self, group) -> bool:
        query = """
        SELECT 1
        FROM group_users
        WHERE group_id = ? AND user_id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (group.id, self.id))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def link_me_with_from_group(self, group) -> "User":

        if self.am_in_group(group):
            if len(group.members()) > 1:
                cursor = self.db_manager.db.cursor()
                # print(f"{user.full_name()} with gender {user.gender}")
                if self.gender is None:
                    query = """
                        SELECT u.*
                        FROM users u
                        JOIN group_users gu ON u.id = gu.user_id
                        WHERE gu.group_id = ? AND u.id != ?
                    """
                    cursor.execute(query, (group.id, self.id))
                else:
                    query = """
                        SELECT u.*
                        FROM users u
                        JOIN group_users gu ON u.id = gu.user_id
                        WHERE gu.group_id = ? AND u.id != ? AND u.gender != ?
                        """
                    cursor.execute(query, (group.id, self.id, self.gender))
                candidates = cursor.fetchall()
                selected_row = random.choice(candidates)
                proposed_user = User()
                proposed_user.load_object_from_row(selected_row)
                return proposed_user
            else:
                print(
                    f"{self.full_name()} is the only member of group {group.groupname}"
                )
                return None

        else:
            print(f"{self.full_name()} is not a member of group {group.groupname}")
            return None
