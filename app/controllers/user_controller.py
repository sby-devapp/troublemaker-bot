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
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("propose", self.propose))

    def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Command handler for /start command.
        """
        user = self.get_user(update, context)
        chat = self.get_chat(update, context)
        welcome_message = f"Welcome {user.full_name} to the chat {chat.title}!"
        context.bot.send_message(chat_id=chat.id, text=welcome_message)

    def propose(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Command handler for /propose command.
        """
        member = self.get_random_user_except(update, context)
        if member:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Proposing {member.user.full_name} for the next task!",
            )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="No suitable members found for proposing.",
            )

    def reload(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Command handler for /reload command. get all users from the group in the chat into the database.
        """
        group_members = context.bot.get_chat_members(chat_id=update.effective_chat.id)
        # get a random user from the group except the bots and the user who sent the command
        for member in group_members:
            if not member.user.is_bot:
                user = self.userService.get_or_create_user(member.user)
                self.userService.save_user(user)

    def get_random_user_except(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """
        Get group members who are not bots and not the user who sent the command.
        """
        group_members = context.bot.get_chat_members(chat_id=update.effective_chat.id)
        # get a random user from the group except the bots and the user who sent the command
        members = []
        for member in group_members:
            if not member.user.is_bot and member.user.id != update.effective_user.id:
                members.append(member)
        # return a random user from the members list
        if members:
            random_member = random.choice(members)
            return random_member
