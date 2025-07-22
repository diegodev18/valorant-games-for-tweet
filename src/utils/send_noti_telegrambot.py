import asyncio
from sys import platform
from telegram import Bot
from get_env import get_env
from send_getcode_exportcode import get_code

(
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    if "win" in platform
    else None
)


async def send(message: str, bot_token: str, chat_id: str):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


def send_message(message: str):
    TELEGRAM_BOT_TOKEN = get_env("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = get_env("TELEGRAM_CHAT_ID")

    asyncio.run(send(message, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID))


if __name__ == "__main__":
    telegram_codes = get_code()
    try:
        send_message("TWEET PUBLICADO EXITOSAMENTE")
    except Exception as e:
        print("Error:", e)
