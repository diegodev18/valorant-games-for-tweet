from time import sleep
from datetime import datetime
from os import system
from platform import platform
from get_twitter_api import get_api_main
from make_tweet import make_tweet_main
from get_times import get_sleep_time
from send_getcode_exportcode import get_code
from send_noti_telegrambot import send_telegram_main

telegram_codes = get_code('telegram_api.pkl') # {'bot_token': bot_token, 'chat_id': chat_id}


def main():
    system('cls' if 'windows' in platform().lower() else 'clear')
    oauth = get_api_main()
    while True:
        games_time = get_sleep_time(day=datetime.now().day+1, hour=1)
        print(f'Esperando tiempo para CREAR el tweet... {games_time} segundos!\n')
        sleep(games_time)

        tweet = make_tweet_main(datetime.now().day)
        print(f'TWEET CREADO\n{tweet}\n')
        send_telegram_main(f'TWEET CREADO EXITOSAMENTE!\n\n{tweet}\n\nESPERANDO TIEMPO: {games_time}' if tweet else 'NO HAY PARTIDOS EL DIA DE HOY :(', 
                           telegram_codes['bot_token'], telegram_codes['chat_id'])

        tweet_time = get_sleep_time(day=datetime.now().day, hour=11)
        print(f'\nEsperando tiempo para SUBIR el tweet... {tweet_time} segundos!')
        sleep(tweet_time)

        if tweet:
            # print('\n' + tweet + '\n')
            response = oauth.post(
                "https://api.twitter.com/2/tweets",
                json={'text': tweet},
            )
            if response.status_code != 201:
                raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
            else:
                print("Response code: ", response.status_code)
                print("Tweet hecho con exito")
                send_telegram_main('TWEET PUBLICADO EXITOSAMENTE', telegram_codes['bot_token'], telegram_codes['chat_id'])

        else:
            print('No hay juegos hoy :(')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
    except Exception as e:
        print('Ah ocurrido un error en el script!')
        send_telegram_main(f'Ah ocurrido un error en el script!\n\n{e}', telegram_codes['bot_token'], telegram_codes['chat_id'])
