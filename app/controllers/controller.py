from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.services.chat_service import ChatService
from app.services.user_service import UserService
from app.models.question import Question
import random

from app.views.poll_view import PollView

# Make sure to import or define ChatService and UserService
# from app.services.chat_service import ChatService
# from app.services.user_service import UserService


class Controller:
    def __init__(self, application):
        self.application = application
        self.chatService = ChatService()
        self.userService = UserService()

    def setup(self):
        print("Setting up the controller")

    def get_chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Returns the chat object from the update.
        """
        chat = update.effective_chat
        return self.chatService.save(chat)

    def get_user(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Returns the chat object from the update.
        """
        user = update.effective_user
        return self.userService.save(user)

    def get_user_chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Saves the user and chat information from the update.
        """
        return self.get_user(update, context), self.get_chat(update, context)

    async def _is_admin_owner(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> bool:
        """
        Checks if the user is an admin or owner in the chat.
        Returns True if admin/owner, False otherwise.
        """
        chat = update.effective_chat
        user = update.effective_user
        if chat.type not in ["group", "supergroup"]:
            return False
        member = await context.bot.get_chat_member(chat.id, user.id)
        return member.status in ["administrator", "creator"]

    def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Command handler for /start command.
        """
        user = self.get_user(update, context)
        chat = self.get_chat(update, context)
        welcome_message = f"Welcome {user.full_name()} to the chat {chat.title}!"
        context.bot.send_message(chat_id=chat.id, text=welcome_message)

    def setup_handlers(self):
        """
        Sets up command handlers for the application.
        """
        self.application.add_handler(CommandHandler("start", self.start))
        # Add more handlers as needed
