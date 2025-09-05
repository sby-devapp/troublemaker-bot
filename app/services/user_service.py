from app.models.user import User


class UserService:
    def __init__(self):
        print("User service initialized")

    def save(self, user) -> User:
        user_db = User(id=user.id).get()
        user_db.id = user.id
        user_db.username = user.username
        user_db.first_name = user.first_name
        user_db.last_name = user.last_name
        return user_db.save()

    def get_by_username(self, username: str) -> User:
        """
        Retrieve a user by their username.
        """
        return User.get_by_username(username)

    def get_by_id(self, user_id: int) -> User:
        """
        Retrieve a user by their ID.
        """
        return User(id=user_id).get()
