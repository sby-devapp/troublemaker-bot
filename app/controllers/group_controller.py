import asyncio
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.controllers.controller import Controller
from app.models.user import User


class GroupController(Controller):

    def __init__(self, application):
        super().__init__(application)

    def setup(self):
        self.application.add_handler(CommandHandler("register", self.handle_register))
        self.application.add_handler(CommandHandler("gossip", self.handle_gossip))
        self.application.add_handler(CommandHandler("crush", self.handle_crush))
        self.application.add_handler(CommandHandler("propose", self.handle_propose))

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
        group = self.get_group(update, context)

        # Case 1: Reply to a message
        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            target_user = self.userService.save(target_user)
        # Case 2: /gossip @username
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = User.get_by_username(username)
                if not target_user:
                    await update.message.reply_text(
                        "User not found. or not registered yet. reply to his message by /register command."
                    )
                    return
            else:
                await update.message.reply_text(
                    f"Usage: /gossip @username or reply to a message with /gossip."
                )
                return

        if not self.groupService.has_member(target_user):
            await update.message.reply_text("User is not registered in this group.")
            return

        # Generate gossip message
        target_user, message = self.groupService.gossip(target_user)
        entities = (
            f"\n[@{target_user.username}]"
            if target_user.username
            else f"\ntg://user?id={target_user.id}"
        )
        print(f"[handle_gossip]: {message}")
        await update.message.reply_text(
            text=message + entities, reply_to_message_id=None
        )

    async def handle_crush(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle crush command in the group."""
        """
        User can execute /crush to get his/her crush, or /crush @username, or reply to a message with /crush.
        In all cases, check if the user exists in the group.
        If yes, generate a random crush line from the database.
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
        group = self.get_group(update, context)

        # Case 1: Reply to a message
        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            target_user = self.userService.save(target_user)
        # Case 2: /crush @username
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = User.get_by_username(username)
            # Case 3: /crush (no argument) - use sender as target
            else:
                target_user = update.effective_user
                target_user = self.userService.save(target_user)

        if not target_user:
            await update.message.reply_text(
                "User not found or not registered yet. Reply to their message with /register command."
            )
            return

        if not self.groupService.has_member(target_user):
            await update.message.reply_text("User is not registered in this group.")
            return

        # Generate crush message
        user, crush, message = self.groupService.crush(target_user)
        entities = "\n"
        entities += (
            f"[@{user.username}]" if crush.username else f"tg://user?id={user.id}"
        )
        print(f"[handle_crush]: {message}")
        message += entities
        await context.bot.send_chat_action(update.effective_chat.id, "typing")
        await asyncio.sleep(2)  # Wait 2 seconds
        await update.message.reply_text(text=message)

    async def handle_propose(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle propose command in the group."""
        """
        User can execute /propose to get a proposal, or /propose @username, or reply to a message with /propose.
        In all cases, check if the user exists in the group.
        If yes, generate a random proposal line from the database.
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
        group = self.get_group(update, context)

        # Case 1: Reply to a message
        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            target_user = self.userService.save(target_user)
        # Case 2: /propose @username
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = User.get_by_username(username)
            # Case 3: /propose (no argument) - use sender as target
            else:
                target_user = update.effective_user
                target_user = self.userService.save(target_user)

        if not target_user:
            await update.message.reply_text(
                "User not found or not registered yet. Reply to their message with /register command."
            )
            return

        if not self.groupService.has_member(target_user):
            await update.message.reply_text("User is not registered in this group.")
            return

        # Generate proposal message
        user, proposed_user, message = self.groupService.propose(target_user)
        entities = (
            f"\n[@{proposed_user.username}, @{user.username}]"
            if proposed_user.username
            else ""
        )
        print(f"[handle_propose]: {message}")
        await update.message.reply_text(
            text=message + entities, reply_to_message_id=None
        )
