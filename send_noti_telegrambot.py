import asyncio
from telegram import Bot
from send_getcode_exportcode import get_code


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def send_message(message: str, bot_token: str, chat_id: str):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


def send_telegram_main(message: str, bot_token: str, chat_id: str):
    asyncio.run(send_message(message, bot_token, chat_id))


if __name__ == '__main__':
    telegram_codes = get_code('telegram_api.pkl')
    try:
        send_telegram_main('TWEET PUBLICADO EXITOSAMENTE', telegram_codes['bot_token'], telegram_codes['chat_id'])
    except Exception as e:
        print()
    print('Amigazo')