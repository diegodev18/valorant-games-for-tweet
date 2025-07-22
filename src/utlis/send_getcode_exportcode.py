from os import environ
from sys import exit

from dotenv import load_dotenv


def get_code():
    load_dotenv()

    if "TELEGRAM_BOT_TOKEN" not in environ:
        print("TELEGRAM_BOT_TOKEN no encontrado en el archivo .env")
        exit(-1)

    if "TELEGRAM_CHAT_ID" not in environ:
        print("TELEGRAM_CHAT_ID no encontrado en el archivo .env")
        exit(-1)

    return {
        "TELEGRAM_BOT_TOKEN": environ.get("TELEGRAM_BOT_TOKEN"),
        "TELEGRAM_CHAT_ID": environ.get("TELEGRAM_CHAT_ID"),
    }  # {'bot_token': bot_token, 'chat_id': chat_id}


if __name__ == "__main__":
    print(get_code())
