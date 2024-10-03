from datetime import datetime
from os import system
from platform import platform
from time import sleep

from make_tweet import make_tweet_main
from get_times import get_sleep_time


def main():
    # Clean screen
    system('cls' if 'windows' in platform().lower() else 'clear')

    # Making the request
    while True:
        games_time = get_sleep_time(day=datetime.now().day + 1, hour=1)
        print(f'Esperando tiempo para CREAR el tweet... {games_time} segundos!\n')

        tweet = make_tweet_main(datetime.now().day+1)  # Crea el tweet (No lo sube)

        tweet_time = get_sleep_time(day=datetime.now().day, hour=20)
        print(f'\nEsperando tiempo para SUBIR el tweet... {tweet_time} segundos!')
        # sleep(tweet_time)

        if tweet:
            print('\n' + tweet + '\n')
        else:
            print('No hay juegos hoy :(')
        break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
