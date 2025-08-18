from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.controllers.controller import Controller


class GroupController(Controller):

    def __init__(self, application):
        super().__init__(application)

    def setup(self):
        self.application.add_handler(CommandHandler("register", self.handle_register))
        self.application.add_handler(CommandHandler("gossip", self.handle_gossip))

    async def handle_register(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle user registration in the group. useing replying on message by /register command."""
        """
        user can register in the group by executing /register command.
        user can register another user by replying to the message of that user with /register command.
        """

        if not self.is_group(update, context):
            await update.message.reply_text(
                "This command can only be used in a group chat."
            )
            return
        print(
            f"[executing] {update.message.text} in {update.effective_chat.title} by {update.effective_user.full_name}"
        )
        # Get user from the replied message or from the command sender
        if update.message.reply_to_message:
            user = update.message.reply_to_message.from_user
        else:
            user = update.effective_user
        user = self.userService.save(user)

        group = self.get_group(update, context)
        self.groupService.register(user)
        message = (
            f"{user.full_name()} has been registered in the group {group.groupname}."
        )
        print("[handle_register] " + message)
        await update.message.reply_text(message)

    async def handle_gossip(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle gossip command in the group."""
        """
        User can execute /gossip @username or reply to a message with /gossip.
        In both cases, check if the user exists in the group.
        If yes, generate a random gossip line from the database and replace {user} with the target user's name.
        """
        if not self.is_group(update, context):
            await update.message.reply_text(
                "This command can only be used in a group chat."
            )
            return

        print(
            f"[executing] {update.message.text} in {update.effective_chat.title} by {update.effective_user.full_name}"
        )

        target_user = None

        # Case 1: Reply to a message
        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            self.userService.save(target_user)
        # Case 2: /gossip @username
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = self.userService.get_by_username(username)

        if not target_user:
            await update.message.reply_text("User not found.")
            return

        group = self.get_group(update, context)
        if not self.groupService.is_user_in_group(target_user):
            await update.message.reply_text("User is not registered in this group.")
            return

        # Get a random gossip line and replace {user} with the target user's name
        gossip_line = self.groupService.get_random_gossip_line(target_user)
        if not gossip_line:
            await update.message.reply_text("No gossip lines available.")
            return

        message = gossip_line.replace("{user}", target_user.full_name)
        print(f"[handle_gossip] {target_user.full_name} : {message}")
        await update.message.reply_text(message)
