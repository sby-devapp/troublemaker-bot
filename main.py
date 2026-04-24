# File: main.py

from telegram.ext import ApplicationBuilder
from app.controllers.user_controller import UserController
from app.controllers.group_controller import GroupController
from app.controllers.listener_controller import ListenerController
from app.models.database.db_manager import DBManager
from bot_token import get_token

DBManager.connect()
# DBManager.initialize()
# build the application with the bot token
app = ApplicationBuilder().token(get_token()).build()

# Initialize controllers in order
listenerController = ListenerController(app)
listenerController.setup()

userController = UserController(app)
userController.setup()

groupController = GroupController(app)
groupController.setup()


if __name__ == "__main__":
    print("Starting the bot...")
    app.run_polling()
