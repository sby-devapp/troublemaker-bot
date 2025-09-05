import os


def get_token():
    return os.environ.get("TELEGRAM_BOT_TOKEN")
