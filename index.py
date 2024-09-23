from time import sleep
from datetime import datetime
from os import system
from platform import platform
from get_twitter_api import get_api_main
from make_tweet import make_tweet_main
from get_times import get_sleep_time


def main():
    system('cls' if 'windows' in platform().lower() else 'clear')
    oauth = get_api_main()
    while True:
        games_time = get_sleep_time(day=datetime.now().day+1, hour=1)
        print(f'Esperando tiempo para CREAR el tweet... {games_time} segundos!\n')
        sleep(games_time)

        tweet = make_tweet_main()

        tweet_time = get_sleep_time(hour=11)
        print(f'\nEsperando tiempo para SUBIR el tweet... {tweet_time} segundos!')
        sleep(tweet_time)

        if tweet:
            print('\n' + tweet + '\n')
            response = oauth.post(
                "https://api.twitter.com/2/tweets",
                json={'text': tweet},
            )
            if response.status_code != 201:
                raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
            else:
                print("Response code: ", response.status_code)
                print("Tweet hecho con exito")
        else:
            print('No hay juegos hoy :(')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
