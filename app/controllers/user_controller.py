from random import random
from telegram import Update
from app.controllers.controller import Controller
from telegram.ext import ContextTypes, CommandHandler

from app.services.user_service import UserService


class UserController(Controller):
    def __init__(self, application):
        super().__init__(application)
        self.userService = UserService()

    def setup(self):
        print("Setting up the user controller")
        self.application.add_handler(CommandHandler("start", self.handle_start))
        self.application.add_handler(CommandHandler("setgender", self.handle_setgender))

    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Command handler for /start command.
        """
        user = self.get_user(update, context)
        chat = self.get_chat(update, context)
        welcome_message = f"Welcome {user.full_name} to the chat {chat.title}!"
        await context.bot.send_message(chat_id=chat.id, text=welcome_message)

    async def handle_setgender(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """
        Command handler for /setgender [gender] command.
        gender can be M/F
        """
        if not update.message.text:
            update.message.reply_text

        user = self.get_user(update, context)
        gender_options = ["M", "F"]
        if (
            len(update.message.text.split()) == 2
            and update.message.text.split()[1].upper() in gender_options
        ):
            user.gender = update.message.text.split()[1].upper()
            user.save()
            update.message.reply_text(f"Gender set to {user.gender}")
        else:
            await update.message.reply_text(
                """something went wrong, please use :
                /setgender M
                or
                /setgender F
                """
            )
