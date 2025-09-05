from app.models.chat import Chat


class ChatService:
    def __init__(self):
        print("Chat service initialized")

    def save(self, chat) -> Chat:
        """
        loads the chat from the database and updates it with the new data.
        If the chat does not exist, it creates a new one.
        """
        chat_db = Chat(id=chat.id).get()
        chat_db.title = chat.title
        chat_db.type = chat.type
        return chat_db.save()

    def get_random_question(self, settings=None):
        return Chat.get_random_question(settings)
