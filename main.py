# File: main.py

from telegram.ext import ApplicationBuilder
from app.controllers.user_controller import UserController
from app.models.database.db_manager import DBManager
from bot_token import get_token

DBManager.connect()
# build the application with the bot token
app = ApplicationBuilder().token(get_token()).build()

# Initialize the chat controller and set it up
userController = UserController(app)
userController.setup()


if __name__ == "__main__":
    print("Starting the bot...")
    app.run_polling()
