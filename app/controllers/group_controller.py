import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, CommandHandler
from app.controllers.controller import Controller
from app.models.user import User


class GroupController(Controller):
    def __init__(self, application):
        super().__init__(application)

    def setup(self):
        self.application.add_handler(CommandHandler("register", self.handle_register))
        self.application.add_handler(CommandHandler("participate", self.handle_participate))
        self.application.add_handler(CommandHandler("logout", self.handle_logout))
        self.application.add_handler(CommandHandler("gossip", self.handle_gossip))
        self.application.add_handler(CommandHandler("propose", self.handle_propose))
        self.application.add_handler(CommandHandler("crush", self.handle_crush))

    async def handle_register(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Register user in the group game (by self or via reply)."""
        print(f"[GroupController] Executing /register in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return
        
        await self.user_info_verification(self.get_user(update, context), update)

        # Get target user
        if update.message.reply_to_message:
            user = update.message.reply_to_message.from_user
        
        else:
            user = update.effective_user

        target_user = self.userService.save(user)
        if target_user.isBot():
            await update.message.reply_text(
                text=(
                    "🤖 Ooh… Are you serious? You want to register a <b>bot</b> in the game?\n"
                    "Try it with a human next time!"
                ),
                parse_mode="HTML"
            )
            return

        group = self.get_group(update, context)
        self.groupService.register(user)

        message = (
            f"<b>{user.full_name()}</b> has been registered in the game in this group.\n"
            f"Use <code>/profile</code> to set your age and gender for a better experience."
        )
        if not user.gender:
            message += "\n\n🔔 <i>Tip: Set your gender in /profile to unlock more features!</i>"

        await update.message.reply_text(message, parse_mode="HTML")

    async def handle_participate(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """User joins the game in the group."""
        print(f"[GroupController] Executing /participate in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return

        user = self.get_user(update, context)
        group = self.get_group(update, context)
        self.groupService.participate_to_game(user, True)

        await update.message.reply_text(
            text=f"<b>{user.full_name()}</b> is now participating in the game! 🎉",
            parse_mode="HTML"
        )

    async def handle_logout(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """User leaves the game in the group."""
        print(f"[GroupController] Executing /logout in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return

        user = self.get_user(update, context)
        group = self.get_group(update, context)
        self.groupService.participate_to_game(user, False)

        await update.message.reply_text(
            text=f"<b>{user.full_name()}</b> has left the game. 😔",
            parse_mode="HTML"
        )

    async def handle_gossip(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Gossip about a user (by reply or @username)."""
        print(f"[GroupController] Executing /gossip in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return

        await self.force_participation(update, context)
        await self.user_info_verification(self.get_user(update, context), update)


        target_user = None
        group = self.get_group(update, context)

        # Case 1: Reply to message
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
                        "❌ User not found or not registered in the game. "
                        "Reply to their message with <code>/register</code>.",
                        parse_mode="HTML"
                    )
                    return
            else:
                await update.message.reply_text(
                    "UsageId: <code>/gossip @username</code> or reply to a message with <code>/gossip</code>.",
                    parse_mode="HTML"
                )
                return
           
        if target_user.isBot():
            await update.message.reply_text(
                text=(
                    "🤖 I’d like to remind you: I’m a bot, not a human.\n"
                    "Did your crush text you or something? Your mind’s clearly on vacation. 😂"
                ),
                parse_mode="HTML"
            )
            return
        
        
        if not self.groupService.has_member(target_user):
            await update.message.reply_text("❌ User is not registered in this group.")
            return

        if not self.groupService.is_participant(target_user):
            await update.message.reply_text(
                text=f"⚠️ <b>{target_user.full_name()}</b> is not participating in the game yet.",
                parse_mode="HTML"
            )
            return

        # Generate gossip
        target_user, message = self.groupService.gossip(target_user)
        username_ref = f"@{target_user.username}" if target_user.username else f"<a href='tg://user?id={target_user.id}'>{target_user.full_name()}</a>"
        final_message = f"{message}\n\n👤 {username_ref}"

        await update.message.reply_text(
            text=final_message,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    async def handle_propose(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Generate a fake proposal message."""
        print(f"[GroupController] Executing /propose in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return

        await self.force_participation(update, context)
        await self.user_info_verification(self.get_user(update, context), update)


        target_user = None
        group = self.get_group(update, context)

        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            target_user = self.userService.save(target_user)
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = User.get_by_username(username)
            else:
                target_user = update.effective_user
                target_user = self.userService.save(target_user)
        if target_user.isBot():
            await update.message.reply_text(
                text=(
                    "🤖 ERROR 404: Romantic feelings not found.\n"
                    "I run on electricity, not emotions, I'm a bot not human ⚡.\n"
                    "Go touch grass — or go take your medicine — maybe the sun was too bright today. ☀️😅"
                ),
                parse_mode="HTML"
            )
            return

        if not target_user:
            await update.message.reply_text(
                "❌ User not found or not registered. Use <code>/register</code> to add them.",
                parse_mode="HTML"
            )
            return

        if not self.groupService.has_member(target_user):
            await update.message.reply_text("❌ User is not registered in this group.")
            return
        
        

        target_user, proposed_user, message = self.groupService.propose(target_user)
        # add the usernames of the target_user and the proposed_user to tag them in the messaage
        entities = ""
        entities += f"{target_user.get_username()}, {proposed_user.get_username()}"
        final_message = message+ "\n\n"+entities

        await update.message.reply_text(
            text=final_message,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    async def handle_crush(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show who has a crush on the user."""
        print(f"[GroupController] Executing /crush in '{update.effective_chat.title}' by {update.effective_user.full_name}")

        if not self.is_group(update, context):
            await update.message.reply_text("This command can only be used in a group chat.")
            return

        await self.force_participation(update, context)
        await self.user_info_verification(self.get_user(update, context), update)


        target_user = None
        group = self.get_group(update, context)

        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
            target_user = self.userService.save(target_user)
        else:
            args = update.message.text.split()
            if len(args) > 1 and args[1].startswith("@"):
                username = args[1][1:]
                target_user = User.get_by_username(username)
            else:
                target_user = update.effective_user
                target_user = self.userService.save(target_user)

        if not target_user:
            await update.message.reply_text(
                "❌ User not found. Use <code>/register</code> to add them.",
                parse_mode="HTML"
            )
            return
        
        if target_user.isBot():
            await update.message.reply_text(
                text=(
                    "🤖 Ooh… Are you serious? Do <b>bots</b> even have crushes ?\n"
                    "Maybe <i>you</i> have a crush on me … 😏\n"
                    "Try it with a human next time!"
                ),
                parse_mode="HTML"
            )
            return

        if not self.groupService.has_member(target_user):
            await update.message.reply_text("❌ User is not registered in this group.")
            return

        user, crush, message = self.groupService.crush(target_user)
        await context.bot.send_chat_action(update.effective_chat.id, "typing")
        await asyncio.sleep(5)

        await update.message.reply_text(
            text=message,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    async def force_participation(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Automatically enroll the user in the game if not already participating.
        Send a private message with a button to jump to the group.
        """
        # Get group and user
        this_group = self.get_group(update, context)
        this_user = self.get_user(update, context)

        # Check if user is already a participant
        if not this_group.is_participant(this_user):
            # Enroll user in the game
            this_group.participate_to_game(this_user, True)

            # Create deep link to the group
            # tid = Telegram ID (e.g., -1001234567890)
            clean_group_id = str(this_group.id).replace("-100", "")
            group_link = f"https://t.me/c/{clean_group_id}"

            # Button to open the group
            keyboard = [
                [InlineKeyboardButton("💬 Jump to Group", url=group_link)]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Notification message
            message = (
                f"🎮 <b>You're In!</b>\n\n"
                f"You’ve been automatically enrolled in the game in:\n"
                f"🔹 <b>{this_group.groupname}</b>\n\n"
                f"Get ready for fake proposals, spicy gossip, and crush alerts! 😈"
                f"LINK: {group_link}"
            )

            try:
                await context.bot.send_message(
                    chat_id=this_user.id,
                    text=message,
                    parse_mode="HTML",
                    reply_markup=reply_markup
                )
            except Exception as e:
                print(f"[force_participation] Could not send PM to user {this_user.id}: {e}")
