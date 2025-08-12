from app.models.chat import Chat


class ChatService:
    def __init__(self):
        print("Chat service")

    def save(self, chat) -> Chat:
        chat_db = Chat(
            id=chat.id,
            type=chat.type,
            username=chat.username,
        )
        return chat_db.save()

    def get_random_question(self, settings=None):
        return Chat.get_random_question(settings)
