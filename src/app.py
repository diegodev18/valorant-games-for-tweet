from datetime import datetime, timedelta
from os import system
from platform import platform
from time import sleep
from sys import exit
from utils import get_sleep_time, x_auth, make_tweet_main, send_message, get_env

env_production = get_env("PYTHON_ENV") == "production"


def main():
    oauth = x_auth()
    send_message('SCRIPT "VALORANG_GAMES_FOR_TWEET" INICIADO CON EXITO!')
    system("cls" if "windows" in platform().lower() else "clear")
    while True:
        games_time = get_sleep_time(day=datetime.now().day + 1, hour=8) if env_production else 10
        msg = (
            f"Esperando tiempo para CREAR el tweet... Se CREARA el {datetime.now() + timedelta(0, games_time)}!\n"
            if games_time
            else "NO HAY PARTIDOS EL DIA DE HOY :("
        )
        print(msg)
        send_message(msg)
        sleep(games_time)

        tweet = make_tweet_main(datetime.now().day)
        print(f"TWEET CREADO\n{tweet}\n")

        tweet_time = get_sleep_time(day=datetime.now().day, hour=18) if env_production else 10
        msg = (
            f"\nEsperando tiempo para SUBIR el tweet... Se SUBIRA el {datetime.now() + timedelta(0, tweet_time)}!\n"
            if tweet
            else "NO HAY PARTIDOS EL DIA DE HOY :("
        )
        print(msg)
        send_message(f"TWEET CREADO EXITOSAMENTE\n\n{tweet}\n{msg}")
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
                send_message("TWEET PUBLICADO EXITOSAMENTE")
                sleep(15)
        else:
            print("No hay juegos hoy :(")


if __name__ == "__main__":
    if env_production:
        while True:
            try:
                main()
            except KeyboardInterrupt:
                print("\nAdios!")
                send_message('SCRIPT "VALORANG_GAMES_FOR_TWEET" FINALIZADO CON EXITO!')
                break
            except Exception as error:
                error_msg = error.with_traceback(None)
                print(f"Ah ocurrido un error en el script!\n{error_msg}")
                send_message(f"Ah ocurrido un error en el script!\n\nERROR:\n{error_msg}")
                sleep(24 * 60 * 60)
    else:
        main()
