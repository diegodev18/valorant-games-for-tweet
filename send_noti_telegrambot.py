import asyncio
from telegram import Bot
from send_getcode_exportcode import get_code
from sys import platform
from os import environ
from dotenv import load_dotenv

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) if 'win' in platform else None


async def send_message(message: str, bot_token: str, chat_id: str):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


def send_telegram_main(message: str):
    load_dotenv()
    TELEGRAM_BOT_TOKEN = environ.get('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = environ.get('TELEGRAM_CHAT_ID')
    
    asyncio.run(send_message(message, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID))


if __name__ == '__main__':
    telegram_codes = get_code()
    try:
        send_telegram_main('TWEET PUBLICADO EXITOSAMENTE')
    except Exception as e:
        print('Error:', e)