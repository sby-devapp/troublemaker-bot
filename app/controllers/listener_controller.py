import random
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters, BaseHandler
from app.controllers.controller import Controller


class ListenerController(Controller):
    def __init__(self, application):
        super().__init__(application)
        self.message_count = {}  # Track message count per group
        self.trigger_threshold = 3  # Default threshold

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
        # Later, we can make this threshold dynamic based on group activity (settings or random)
        self.trigger_threshold = random.randint(3, 7)