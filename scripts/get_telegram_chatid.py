from dotenv import load_dotenv
from os import getenv
from requests import get

load_dotenv()


def get_updates_url(BOT_TOKEN: str | None):
    if not BOT_TOKEN:
        return None
    return f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"


def get_chatid(BOT_TOKEN: str | None, first_name=None):
    url = get_updates_url(BOT_TOKEN)
    if not url:
        print("No se ha proporcionado el token del bot")
        return None

    response = get(url)
    data = response.json()

    print("Datos recibidos:", data, sep="\n")

    if response.status_code == 200:
        if len(data["result"]) > 0:
            if first_name:
                lower_name = first_name.lower()
                for i in data["result"]:
                    if i["message"]["from"]["first_name"].lower() == lower_name:
                        chat_id = i["message"]["chat"]["id"]
                        print(f"Chat ID de {first_name}: {chat_id}")
                        return chat_id
            else:
                chat_id = data["result"][-1]["message"]["chat"]["id"]
                print(f"Chat ID del último usuario: {chat_id}")
                return chat_id

    print("No se pudo obtener el chat ID")
    return None


if __name__ == "__main__":
    BOT_TOKEN: str | None = getenv("TELEGRAM_BOT_TOKEN")
    get_chatid(BOT_TOKEN, "Diego")
