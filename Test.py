from time import sleep
from datetime import datetime
from os import system
from platform import platform
from random import choice
from get_files import get_file
from upload_item_to_write import upload_items
import get_games_from_file
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

    # Making the request
    target = {'hour': 11, 'minute': 0, 'second': 0, 'microsecond': 0}
    emotes = "⌚🥵🤩🪐🍫🎬🤟🤯👏🔥🚀💣🎇🔫☣️☕🌭☀️"
    while True:
        # Check time
        now = datetime.now()
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
                    any(tournament in game['server'] for tournament in tournaments)) and
                    len(games_today) != 6)):
                games_today.append(f"{game['server']} | {game['left']} vs {game['right']}")
                checked_games.append(game)
        upload_items(checked_games, 'history.txt')
        if len(games_today) > 1:
            tweet = '\n'.join(games_today)
            print('\n' + tweet + '\n')
        else:
            print('No hay juegos hoy :(')
        sleep(100)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAdios!')
