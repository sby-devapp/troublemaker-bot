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
        if self.is_group(update, context):
            await update.message.reply_text(
                "This command can only be used in a private chat."
            )
            return

        user = self.get_user(update, context)
        welcome_message = (
            f"Welcome {user.full_name()}!\n"
            ""
            "You can set your gender using this command: /setgender [M|F]."
        )
        await update.message.reply_text(welcome_message)

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
        print(f"[handle_setgender] {user.gender} for {user.full_name()}")
        gender_options = ["M", "F"]
        if (
            len(update.message.text.split()) == 2
            and update.message.text.split()[1].upper() in gender_options
        ):
            user.gender = update.message.text.split()[1].upper()
            user._update()
            print(f"[handle_setgender] {user.gender} for {user.full_name()}")
            await update.message.reply_text(f"Gender set to {user.gender}")
        else:
            await update.message.reply_text(
                """Something went wrong, please use :
                /setgender M
                or
                /setgender F
                """
            )
