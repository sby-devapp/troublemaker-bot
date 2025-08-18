from app.models.database.model import Model
from app.models.user import User
import random


class Group(Model):
    table_name = "groups"

    def __init__(self, id=None, groupname=None):
        self.id = id
        self.groupname = groupname
        self._members = []  # List to hold group members

    def _insert(self):
        query = f"""
        INSERT INTO {self.table_name} (id,groupname)
        VALUES (?,?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(
            query,
            (
                self.id,
                self.groupname,
            ),
        )
        return self

    def _update(self):
        query = f"""
        UPDATE {self.table_name}
        SET groupname = ?
        WHERE id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(
            query,
            (
                self.groupname,
                self.id,
            ),
        )
        return self

    def load_object_from_row(self, row):
        if row:
            self.id = row["id"]
            self.groupname = row["groupname"]
            # Assuming the members are stored in a related table, you would load them here

    def add_member(self, member: User):  # member is an instance of User
        # check if member is exists if not then add it
        member.save()  # insert or update member(User) in database
        self.save()  # insert or update group in database
        query = f"""
        INSERT OR IGNORE INTO group_users (group_id, user_id)
        VALUES (?, ?)
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id, member.id))
        if self.is_user_exist(member):
            self._members.append(member)  # Add member to the local list

    def members(self):
        if not self._members:
            self.load_members()
        return self._members

    def load_members(self):
        """Load members from the database into the _members list."""
        query = f"""
            SELECT u.*
            FROM users u
            JOIN group_users gu ON u.id = gu.user_id
            WHERE gu.group_id = ?
            """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id,))
        rows = cursor.fetchall()
        self._members = []
        for row in rows:
            user = User()
            user.load_object_from_row(row)
            self._members.append(user)
        return self._members

    def propose_to(self, user: User) -> User:
        """Propose a user from this group to the user who given in the param ."""
        return user.link_me_with_from_group(self)

    def is_user_exist(self, user: User) -> bool:
        """Check if a user is already a member of the group."""
        """ Check is (group.id,user.id) exist in group_users table """
        query = f"""
        SELECT 1 FROM group_users
        WHERE group_id = ? AND user_id = ?
        """
        cursor = self.db_manager.db.cursor()
        cursor.execute(query, (self.id, user.id))
        return cursor.fetchone() is not None
