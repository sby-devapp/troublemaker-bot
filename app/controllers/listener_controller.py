import random
import asyncio
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters, BaseHandler
from app.controllers.controller import Controller


class ListenerController(Controller):
    def __init__(self, application):
        super().__init__(application)
        self.message_count = {}  # Track message count per group
        self.trigger_threshold = 3  # Default threshold
        self.last_message_time = {}  # Track last message time per group
        self.last_message_from_bot = {}  # Track if last message was from bot
        self.silence_duration = 300  # 5 minutes in seconds
        self.silence_tasks = {}  # Track silence detection tasks per group

    def setup(self):
        # Use highest possible priority (group -10) to ensure we catch ALL messages
        print("[ListenerController] Setting up message handler...")
        self.application.add_handler(
            MessageHandler(filters.ALL, self.handle_message),
            group=-10  # Highest priority - runs before ALL other handlers
        )
        print("[ListenerController] Message handler registered successfully")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Listen to group messages and intervene after N messages."""
        
        if not update.message or not update.effective_user or not update.effective_chat:
            return
        
        # Only process group messages
        if update.effective_chat.type not in ['group', 'supergroup']:
            return

        # Get basic info
        group_id = update.effective_chat.id
        sender = update.effective_user.full_name
        msg_text = update.message.text or "[media/document]"
        is_bot_message = update.effective_user.is_bot
        
        # Update silence tracking
        self.update_silence_tracking(group_id, is_bot_message, context)
        
        # Initialize counter for this group
        if group_id not in self.message_count:
            self.message_count[group_id] = 0

        self.message_count[group_id] += 1
        current_count = self.message_count[group_id]
        
        # Log message in one line
        print(f"[{update.effective_chat.title}] {sender}: {msg_text[:50]:<50} | Count: {current_count}/{self.trigger_threshold}")
        
        # Check if we should trigger an event
        if current_count >= self.trigger_threshold:
            try:
                await self.random_intervention(update, context)
                print(f"✅ Intervention sent in '{update.effective_chat.title}'")
            except Exception as e:
                print(f"❌ Error: {e}")
            
            self.reset_counter(group_id)
            print(f"🔄 Counter reset. New threshold: {self.trigger_threshold}\n")
        
        # Don't return anything to allow other handlers to process this message

    async def random_intervention(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Randomly pick an intervention type."""
        interventions = [
            self.send_reaction,
            self.send_observation,
            self.send_tease
        ]
        
        # Randomly pick an intervention
        intervention = random.choice(interventions)
        await intervention(update, context)

    async def send_reaction(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a random reaction."""
        reactions = ["😂", "👀", "🍿", "💀", "🤔", "👁️‍🗨️", "🌶️"]
        reaction = random.choice(reactions)
        await update.message.reply_text(reaction)

    async def send_observation(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a random observation."""
        observations = [
            "This group is getting spicy! 🌶️",
            "Interesting conversation... 👀",
            "*grabs popcorn* 🍿",
            "Y'all are wild 😂",
            "The drama never stops here! 💀",
            "Someone's about to spill tea ☕",
            "This escalated quickly 📈"
        ]
        observation = random.choice(observations)
        await update.message.reply_text(observation)

    async def send_tease(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a light tease."""
        teases = [
            "Someone's been very quiet today... 👀",
            "I see what's happening here 😏",
            "The group detective is watching 🕵️",
            "Hmm, suspicious activity detected 🤨",
            "Y'all think I'm not paying attention? 😂"
        ]
        tease = random.choice(teases)
        await update.message.reply_text(tease)


    def reset_counter(self, group_id):
        """Reset message counter and set new random threshold."""
        self.message_count[group_id] = 0
        self.trigger_threshold = random.randint(3, 7)
    
    def update_silence_tracking(self, group_id, is_bot_message, context):
        """Update silence tracking for the group."""
        current_time = datetime.now()
        
        # Cancel existing silence task if any
        if group_id in self.silence_tasks:
            self.silence_tasks[group_id].cancel()
        
        # Update tracking
        self.last_message_time[group_id] = current_time
        self.last_message_from_bot[group_id] = is_bot_message
        
        # Start new silence detection task
        self.silence_tasks[group_id] = asyncio.create_task(
            self.check_silence(group_id, context)
        )
    
    async def check_silence(self, group_id, context):
        """Check for silence after specified duration."""
        try:
            await asyncio.sleep(self.silence_duration)
            
            # Check if last message was not from bot
            if not self.last_message_from_bot.get(group_id, True):
                await self.send_silence_breaker(group_id, context)
                
        except asyncio.CancelledError:
            # Task was cancelled due to new message
            pass
    
    async def send_silence_breaker(self, group_id, context):
        """Send a message to break the silence."""
        try:
            # Get random users from the group to mention
            from app.models.user import User
            group_users = User.get_group_participants(group_id)
            
            silence_messages = [
                "Hmm! This group is silent... 🤫",
                "Is this group dead? 💀",
                "Ooh guys, where are you? 👻",
                "*cricket sounds* 🦗",
                "Hello? Anyone there? 📢",
                "Did everyone fall asleep? 😴",
                "The silence is deafening! 🔇"
            ]
            
            mention_messages = [
                "Ooh {user}, long time no see! 👋",
                "Hey {user}, where have you been? 🤔",
                "{user}, come join the conversation! 💬",
                "Missing you in the chat, {user}! 😢",
                "{user}, say something! The group is too quiet 🗣️",
                "Wake up {user}! Time to chat! ⏰"
            ]
            
            if group_users and len(group_users) > 0 and random.choice([True, False]):
                # 50% chance to mention someone
                random_user = random.choice(group_users)
                message = random.choice(mention_messages).format(user=random_user.get_username())
            else:
                # General silence message
                message = random.choice(silence_messages)
            
            await context.bot.send_message(
                chat_id=group_id,
                text=message,
                parse_mode="HTML"
            )
            
            print(f"🔕 Silence breaker sent to group {group_id}: {message}")
            
        except Exception as e:
            print(f"❌ Error sending silence breaker: {e}")