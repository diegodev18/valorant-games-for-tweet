from time import sleep
from datetime import datetime
from os import system
from platform import platform
from random import choice
from get_files import get_file
from get_twitter_api import get_api_main
from upload_item_to_write import upload_items
import get_games_from_file
import get_online_games


def main():
    # Clean screen
    system('cls' if 'windows' in platform().lower() else 'clear')

    oauth = get_api_main()

    # Making the request
    target = {'hour': 11, 'minute': 0, 'second': 0, 'microsecond': 0}
    emotes = "⌚🥵🤩🪐🍫🎬🤟🤯👏🔥🚀💣🎇🔫☣️☕🌭☀️"
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
        # Get from files
        frases = get_file('frases.txt')
        arrobas = get_file('arrobas.txt')
        tournaments = get_file('tournaments.txt')
        # Start function
        games_today = [f"{choice(frases)} {choice(['en', 'para'])} @{choice(arrobas)} {choice(emotes)}\n"]
        checked_games = []
        get_online_games.main()
        games = get_games_from_file.main()
        for game in games:
            if (((game['date'].day == now.day and
                    any(tournament in game['server'].split(' ') for tournament in tournaments)) and
                    len(games_today) != 6)):
                games_today.append(f"{game['server']} | {game['left']} vs {game['right']}")
                checked_games.append(game)
        upload_items(checked_games, 'history.txt')
        if len(games_today) > 1:
            tweet = '\n'.join(games_today)
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
