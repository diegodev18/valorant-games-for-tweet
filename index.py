from time import sleep
from datetime import datetime
from os import system
from platform import platform
from random import choice
from get_files import get_file
from get_twitter_api import get_api_main
from upload_item_to_write import upload_items
from make_tweet import make_tweet_main
import get_online_games


def main():
    # Clean screen
    system('cls' if 'windows' in platform().lower() else 'clear')

    oauth = get_api_main()

    # Making the request
    target = {'hour': 1, 'minute': 5, 'second': 0, 'microsecond': 0}
    while True:
        # Check time
        now = datetime.now().replace(microsecond=0)
        now_target = now.replace(day=now.day + 1,
                                 hour=target['hour'],
                                 minute=target['minute'],
                                 second=target['second'],
                                 microsecond=target['microsecond'])
        print(f'Esperando reinicio... {(now_target - now).total_seconds()} segundos!\n')
        sleep((now_target - now).total_seconds())
        tweet = make_tweet_main()
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
