from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.models.group import Group
from app.services.chat_service import ChatService
from app.services.group_service import GroupService
from app.services.user_service import UserService
import random


# Make sure to import or define ChatService and UserService
# from app.services.chat_service import ChatService
# from app.services.user_service import UserService


class Controller:
    def __init__(self, application):
        self.application = application
        self.chatService = ChatService()
        self.userService = UserService()
        self.groupService = GroupService()

    def setup(self):
        print("Setting up the controller")
        pass

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

    def is_group(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        """
        Checks if the update is from a group chat.
        """
        return update.effective_chat.type in ["group", "supergroup"]

    def get_group(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Returns the group object from the update.
        """
        chat = update.effective_chat
        if self.is_group(update, context):
            group = Group(id=chat.id, groupname=chat.title)
            group.save()
            self.groupService.group = group

        return self.groupService.group
