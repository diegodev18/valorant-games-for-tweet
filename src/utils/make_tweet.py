from datetime import datetime
from utils.upload_item_to_write import upload_items
from utils.get_games import get_games
from utils.get_data import get_data
from utils.llm import generate_text
import json


def make_tweet_main(day):
    # Start function
    checked_games = get_games()
    upload_items(checked_games, "history.txt")

    if checked_games is None or len(checked_games) == 0:
        return None

    tweet = generate_text(
        f"""\
Crea un tweet en español para anunciar los siguientes partidos de VALORANT.
El tweet debe ser conciso y atractivo, utilizando un lenguaje informal y emojis relacionados con videojuegos y tecnología.
El tweet debe incluir una introducción llamativa y una lista de los partidos con sus fechas y equipos.
Limita el tweet a un máximo de 275 caracteres.

Haz una investigacion rapida para incluir los nombres de los equipos mas populares en la comunidad hispanohablante de VALORANT.

Partidos:
{json.dumps(checked_games, ensure_ascii=False)}

Solo usa los juegos de hoy para crear el tweet.
La fecha de hoy en formato ISO es {datetime.now().isoformat()}.
El target de usuarios es hispanohablante, mas especificamente Mexicano.
"""
    )

    return tweet[:279]


if __name__ == "__main__":
    from datetime import datetime

    try:
        print(f"\n{make_tweet_main(datetime.now().day + 1)}")
    except KeyboardInterrupt:
        print("\nAdios!")
