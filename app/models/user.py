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
        age=None,
        gender=None,
        is_bot="N"
    ):
        super().__init__()
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.is_bot = is_bot

    def isBot(self)-> bool:
        if self.is_bot == "Y":
            return True
        return False
    
    def set_is_bot(self, is_bot=False):
        if is_bot == False:
            self.is_bot = "N"
        elif is_bot == True:
            self.is_bot = "Y"


    def _insert(self):
        if self.id is None:
            print("Error: User id is None. Cannot insert user without id.")
            return None
        fields = []
        placeholders = []
        values = []

        fields.append("id")
        placeholders.append("?")
        values.append(self.id)
        if self.username is not None:
            fields.append("username")
            placeholders.append("?")
            values.append(self.username)
        if self.first_name is not None:
            fields.append("first_name")
            placeholders.append("?")
            values.append(self.first_name)
        if self.last_name is not None:
            fields.append("last_name")
            placeholders.append("?")
            values.append(self.last_name)
        if self.gender is not None:
            fields.append("gender")
            placeholders.append("?")
            values.append(self.gender)
        if self.age is not None:
            fields.append("age")
            placeholders.append("?")
            values.append(self.age)
        if self.is_bot is not None:
            fields.append("is_bot")
            placeholders.append("?")
            values.append(self.is_bot)

        query = f"""
        INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(placeholders)})
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, values)
        cursor.close()
        return self

    def _update(self):
        fields = ["username = ?", "first_name = ?", "last_name = ?"]
        values = [self.username, self.first_name, self.last_name]

        if self.gender is not None:
            fields.append("gender = ?")
            values.append(self.gender)
        if self.age is not None:
            fields.append("age = ?")
            values.append(self.age)
        if self.is_bot is not None:
            fields.append("is_bot = ?")
            values.append(self.is_bot)

        query = f"""
        UPDATE {self.table_name}
        SET {', '.join(fields)}
        WHERE id = ?
        """
        values.append(self.id)
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
        self.age = row["age"]
        self.gender = row["gender"]
        self.is_bot = row["is_bot"]

    def belong_to(self, group) -> bool:
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

        if not group.has_member(self):
            raise ValueError(
                f"The member {self.full_name()} is not exist {group.groupname}"
            )
            return
        if group.count_members() < 2:
            raise ValueError("Thers's no enough members!")
            return

        print(f"[Debbug] we start looking for your soulemate!")
        proposed_user = None
        if self.gender == "M":
            proposed_user = self.get_random_female_user(group)
            print(f"proposed_user 1: {vars(proposed_user)}")
        elif self.gender == "F":
            proposed_user = self.get_random_male_user(group)
            print(f"proposed_user 2: {vars(proposed_user)}")

        if proposed_user is None:
            proposed_user = self.get_random_unknown_gender_user(group)
            print(f"proposed_user 3: {vars(proposed_user)}")
        return proposed_user

    @classmethod
    def get_by_username(cls, username):
        query = f"SELECT * FROM {cls.table_name} WHERE username = ?"
        cursor = cls.db_manager.db.cursor()
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            user = cls()
            user.load_object_from_row(row)
            return user
        return None

    def get_random_female_user(self, group):
        query = """
            SELECT u.*
                FROM users u
            JOIN group_users gu ON u.id = gu.user_id
                WHERE gu.group_id = ? 
                AND u.id != ? 
                AND u.gender = 'F' 
                AND gu.is_participant = 'y';
        """
        cursor = self.db_manager.db.cursor()
        print(
            f"[get_random_male_user] Executing query: {query} with group_id={group.id} and user_id={self.id}"
        )
        cursor.execute(query, (group.id, self.id))
        candidates = cursor.fetchall()
        print(f"Number of condidates: {len(candidates)}")
        cursor.close()
        if not candidates:
            return None
        selected_row = random.choice(candidates)
        proposed_user = User()
        proposed_user.load_object_from_row(selected_row)

        return proposed_user

    def get_random_male_user(self, group):
        query = """
            SELECT u.*
            FROM users u
            JOIN group_users gu ON u.id = gu.user_id
            WHERE gu.group_id = ? 
                AND u.id != ? 
                AND u.gender = 'M' 
                AND gu.is_participant = 'y'
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (group.id, self.id))
        candidates = cursor.fetchall()
        cursor.close()
        if not candidates:
            return None
        selected_row = random.choice(candidates)
        proposed_user = User()
        proposed_user.load_object_from_row(selected_row)
        return proposed_user

    def get_random_unknown_gender_user(self, group):
        query = """
            SELECT u.*
            FROM users u
            JOIN group_users gu ON u.id = gu.user_id
            WHERE gu.group_id = ? 
                AND u.id != ? 
                AND u.gender IS NULL 
                AND gu.is_participant = 'y'
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (group.id, self.id))
        candidates = cursor.fetchall()
        cursor.close()
        print(f"Number of condidates: {len(candidates)}")
        if not candidates:
            return None
        selected_row = random.choice(candidates)
        proposed_user = User()
        proposed_user.load_object_from_row(selected_row)

        return proposed_user

    def get_username(self):
        if self.username == "" or self.username is None:
            return f"tg://id={self.id}"
        else:
            return f"@{self.username}"


