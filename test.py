from datetime import datetime
from os import system
from platform import platform
from time import sleep
from make_tweet import make_tweet_main
from get_times import get_sleep_time
from send_getcode_exportcode import get_code
from send_noti_telegrambot import send_telegram_main

telegram_codes = get_code('telegram_api.pkl')


def main():
    # Clean screen
    system('cls' if 'windows' in platform().lower() else 'clear')

    # Making the request
    while True:
        games_time = get_sleep_time(day=datetime.now().day + 1, hour=1)
        print(f'Esperando tiempo para CREAR el tweet... {games_time} segundos!\n')

        tweet = make_tweet_main(datetime.now().day)  # Crea el tweet (No lo sube)
        
        send_telegram_main(f'TWEET CREADO EXITOSAMENTE!\n\n{tweet}\n\nESPERANDO TIEMPO: {games_time}!' if tweet else f'TWEET CREADO EXITOSAMENTE PERO NO HAY JUEGOS PARA HOY :(', 
                           telegram_codes['bot_token'], telegram_codes['chat_id'])

        tweet_time = get_sleep_time(day=datetime.now().day, hour=20)
        print(f'\nEsperando tiempo para SUBIR el tweet... {tweet_time} segundos!')
        # sleep(tweet_time)

        if tweet:
            print('\n' + tweet + '\n')
            send_telegram_main(f'TWEET SUBIDO EXITOSAMENTE!', telegram_codes['bot_token'], telegram_codes['chat_id'])
        else:
            print('No hay juegos hoy :(')
        break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
    except Exception as e:
        send_telegram_main()
