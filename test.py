from time import sleep
from datetime import datetime
from os import system
from platform import platform
from random import choice
from get_files import get_file
from upload_item_to_write import upload_items
from make_tweet import make_tweet_main
import get_online_games


def upload_items(my_items_to_add: list, name: str):
    try:
        with open(name, 'r') as f:
            my_items = f.read().split('\n')
        f.close()
    except FileNotFoundError:
        my_items = []
    with open(name, 'w') as f:
        if len(my_items) != 0:
            for item in my_items:
                f.write(f'{item}\n')
        f.write(f'{datetime.now()}\n')
        for item in my_items_to_add:
            f.write(f'{item}\n')
    f.close()


def main():
    # Clean screen
    system('cls' if 'windows' in platform().lower() else 'clear')
    while True:
        tweet = make_tweet_main(23)
        if tweet:
            print('\n' + tweet + '\n')
        else:
            print('No hay juegos hoy :(')
        sleep(100)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
