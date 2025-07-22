from datetime import datetime, timedelta
from os import system
from platform import platform
from time import sleep
from src.utils import (
    get_sleep_time,
    get_api_main,
    make_tweet_main,
    get_code,
    send_telegram_main
)

telegram_codes = get_code()  # {'bot_token': bot_token, 'chat_id': chat_id}


def main():
    oauth = get_api_main()
    send_telegram_main('SCRIPT "VALORANG_GAMES_FOR_TWEET" INICIADO CON EXITO!')
    system("cls" if "windows" in platform().lower() else "clear")
    while True:
        games_time = get_sleep_time(day=datetime.now().day + 1, hour=8)
        msg = (
            f"Esperando tiempo para CREAR el tweet... Se CREARA el {datetime.now() + timedelta(0, games_time)}!\n"
            if games_time
            else "NO HAY PARTIDOS EL DIA DE HOY :("
        )
        print(msg)
        send_telegram_main(msg)
        sleep(games_time)

        tweet = make_tweet_main(datetime.now().day)
        print(f"TWEET CREADO\n{tweet}\n")

        tweet_time = get_sleep_time(day=datetime.now().day, hour=18)
        msg = (
            f"\nEsperando tiempo para SUBIR el tweet... Se SUBIRA el {datetime.now() + timedelta(0, tweet_time)}!\n"
            if tweet
            else "NO HAY PARTIDOS EL DIA DE HOY :("
        )
        print(msg)
        send_telegram_main(f"TWEET CREADO EXITOSAMENTE\n\n{tweet}\n{msg}")
        sleep(tweet_time)

        if tweet:
            response = oauth.post(
                "https://api.twitter.com/2/tweets", json={"text": tweet}, timeout=30
            )
            if response.status_code != 201:
                raise Exception(
                    "Request returned an error: {} {}".format(
                        response.status_code, response.text
                    )
                )
            else:
                print("Response code: ", response.status_code)
                print("Tweet hecho con exito")
                sleep(5)
                send_telegram_main("TWEET PUBLICADO EXITOSAMENTE")
                sleep(15)
        else:
            print("No hay juegos hoy :(")


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nAdios!")
            send_telegram_main(
                'SCRIPT "VALORANG_GAMES_FOR_TWEET" FINALIZADO CON EXITO!'
            )
        except Exception as error:
            error_msg = error.with_traceback(None)
            print(f"Ah ocurrido un error en el script!\n{error_msg}")
            send_telegram_main(
                f"Ah ocurrido un error en el script!\n\nERROR:\n{error_msg}"
            )
            sleep(24 * 60 * 60)
