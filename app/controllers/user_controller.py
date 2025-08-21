from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

from app.controllers.controller import Controller
from app.services.user_service import UserService


class UserController(Controller):
    PROFILE, SET_AGE, SET_GENDER = range(3)

    def __init__(self, application):
        super().__init__(application)
        self.userService = UserService()

    def setup(self):
        """Set up the conversation handler for profile management."""
        print("Setting up the user controller")

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("profile", self.handle_profile)],
            states={
                self.PROFILE: [
                    CallbackQueryHandler(self.set_age_prompt, pattern=r"^set_age_"),
                    CallbackQueryHandler(
                        self.set_gender_prompt, pattern=r"^set_gender_"
                    ),
                    CallbackQueryHandler(
                        self.handle_close_profile, pattern=r"^close_profile$"
                    ),
                    CallbackQueryHandler(
                        self.handle_back_to_profile, pattern=r"^back_to_profile$"
                    ),
                ],
                self.SET_AGE: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.save_age),
                    # Allow user to cancel age input
                    CallbackQueryHandler(
                        self.handle_back_to_profile, pattern=r"^back_to_profile$"
                    ),
                    CallbackQueryHandler(
                        self.handle_close_profile, pattern=r"^close_profile$"
                    ),
                ],
                self.SET_GENDER: [
                    CallbackQueryHandler(self.save_gender, pattern=r"^edit_gender_")
                ],
            },
            fallbacks=[],
            per_user=True,
            per_chat=True,
        )

        self.application.add_handler(conv_handler)
        self.application.add_handler(CommandHandler("start", self.handle_start))
        self.application.add_handler(CommandHandler("refresh", self.handle_refresh))

    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command."""
        if self.is_group(update, context):
            await update.message.reply_text(
                "This command can only be used in a private chat."
            )
            return

        user = self.get_user(update, context)
        bot_name = context.bot.name
        welcome_message = (
            f"Welcome {user.full_name()}!\n"
            f"I'm {bot_name}, I'm here only for fun. Don't trust everything I say. 😄\n\n"
            "You can view your profile using the /profile command."
        )
        await update.message.reply_text(welcome_message)

    async def handle_profile(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Entry point: Show profile in private, or deep link if in group."""
        if self.is_group(update, context):
            bot_username = context.bot.username
            # Fixed: Removed extra space in URL
            deep_link = f"https://t.me/{bot_username}?start=profile"
            keyboard = [[InlineKeyboardButton("Open in Private", url=deep_link)]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "This command can only be used in a private chat.\n"
                "Click the button below to open your profile.",
                reply_markup=reply_markup,
            )
            return ConversationHandler.END

        return await self.show_profile(update, context)

    async def show_profile(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show or update the user profile with buttons."""
        user = self.get_user(update, context)
        gender_options = {"M": "Male", "F": "Female"}
        profile_message = (
            f"👤 <b>Profile</b>\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🔹 <b>ID:</b> {user.id}\n"
            f"🔹 <b>Username:</b> @{user.username if user.username else 'Not set'}\n"
            f"🔹 <b>Full Name:</b> {user.full_name()}\n"
            f"🔹 <b>Gender:</b> {gender_options.get(user.gender, 'Not set')}\n"
            f"🔹 <b>Age:</b> {user.age if user.age else 'Not set'}"
        )

        keyboard = [
            [
                InlineKeyboardButton("✏️ Set Age", callback_data=f"set_age_{user.id}"),
                InlineKeyboardButton(
                    "⚧ Set Gender", callback_data=f"set_gender_{user.id}"
                ),
            ],
            [InlineKeyboardButton("❌ Close", callback_data="close_profile")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        try:
            if query:
                await query.edit_message_text(
                    text=profile_message, reply_markup=reply_markup, parse_mode="HTML"
                )
            else:
                await update.message.reply_text(
                    text=profile_message, reply_markup=reply_markup, parse_mode="HTML"
                )
        except Exception:
            # Fallback if text didn't change or message is too old
            await update.message.reply_text(
                text=profile_message, reply_markup=reply_markup, parse_mode="HTML"
            )

        return self.PROFILE

    async def set_age_prompt(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Prompt user to enter age with Back and Close buttons."""
        query = update.callback_query
        await query.answer("Enter your age (16–120)")

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to Profile", callback_data="back_to_profile"
                )
            ],
            [InlineKeyboardButton("❌ Close", callback_data="close_profile")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="🔢 Please enter your age:", reply_markup=reply_markup
        )
        return self.SET_AGE

    async def save_age(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Save the entered age."""
        user = self.get_user(update, context)
        try:
            age = int(update.message.text.strip())
            if not (16 <= age <= 120):
                await update.message.reply_text(
                    "❌ Please enter a valid age between 16 and 120."
                )
                return self.SET_AGE
            user.age = age
            user._update()
            await update.message.reply_text(f"✅ Age set to {age}.")
        except ValueError:
            await update.message.reply_text("❌ Please enter a valid number.")
            return self.SET_AGE

        return await self.show_profile(update, context)

    async def set_gender_prompt(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """Show gender selection with Back button."""
        query = update.callback_query
        await query.answer()
        user_id = int(query.data.split("_")[-1])

        keyboard = [
            [
                InlineKeyboardButton(
                    "🚹 Male", callback_data=f"edit_gender_M_{user_id}"
                ),
                InlineKeyboardButton(
                    "🚺 Female", callback_data=f"edit_gender_F_{user_id}"
                ),
            ],
            [
                InlineKeyboardButton(
                    "🔙 Back to Profile", callback_data="back_to_profile"
                )
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚧ Please select your gender:", reply_markup=reply_markup
        )
        return self.SET_GENDER

    async def save_gender(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Save selected gender."""
        query = update.callback_query
        await query.answer()
        parts = query.data.split("_")

        if len(parts) == 4 and parts[0] == "edit" and parts[1] == "gender":
            gender = parts[2]
            user_id = int(parts[3])
            user = self.userService.get_by_id(user_id)
            if user:
                user.gender = gender
                user._update()
                await query.edit_message_text(
                    f"✅ Gender updated to {gender_options.get(gender, 'Unknown')}."
                )
            else:
                await query.edit_message_text("❌ User not found.")
        else:
            await query.edit_message_text("❌ Invalid request.")

        return await self.show_profile(update, context)

    async def handle_refresh(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Refresh the profile."""
        if self.is_group(update, context):
            await update.message.reply_text("Use /refresh in private chat.")
            return

        await update.message.reply_text("🔄 Refreshing your profile...")
        return await self.show_profile(update, context)

    async def handle_close_profile(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """Close the profile and end the conversation."""
        query = update.callback_query
        await query.answer()
        await query.edit_message_text("✅ Profile closed.")
        return ConversationHandler.END

    async def handle_back_to_profile(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """Go back to profile from any state."""
        query = update.callback_query
        await query.answer("🔙 Returning to profile...")
        try:
            await query.edit_message_text("🔄 Loading your profile...")
        except:
            pass  # Ignore if message can't be edited
        return await self.show_profile(update, context)


# Define gender options globally for reuse
gender_options = {"M": "Male", "F": "Female"}
