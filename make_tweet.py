from datetime import datetime
from random import choice
from get_files import get_file
from upload_item_to_write import upload_items
import get_online_games


def make_tweet_main(day):
    emotes = "⌚🥵🤩🪐🍫🎬🤟🤯👏🔥🚀💣🎇🔫☣️☕🌭☀️"
    # Get from files
    frases = get_file('frases.txt')
    arrobas = get_file('arrobas.txt')
    tournaments = get_file('tournaments.txt')
    # Start function
    games_today = [f"{choice(frases)} {choice(['en', 'para'])} @{choice(arrobas)} {choice(emotes)}\n"]
    checked_games = []
    games = get_online_games.main()
    for game in games:
        if (((game['date'].day == day and
              any(tournament in game['server'].split(' ') for tournament in tournaments)) and
             len(games_today) != 6)):
            games_today.append(f"{game['server']} | {game['left']} vs {game['right']}")
        if any(tournament in game['server'] for tournament in tournaments):
            checked_games.append(f"GAME ON TOURNAMENT LIST:      "
                                 f"{game['server'][:10]} | {game['date']} | {game['left'][:10]} vs {game['right'][:10]}")
        else:
            checked_games.append(f"GAME WITHOUT TOURNAMENT LIST: "
                                 f"{game['server'][:10]} | {game['date']} | {game['left'][:10]} vs {game['right'][:10]}")
    upload_items(checked_games, 'history.txt')
    if len(games_today) > 1:
        tweet = '\n'.join(games_today)[:275]
        tweet = f'{tweet}...'
    else:
        return None
    return tweet


if __name__ == '__main__':
    try:
        print(f'\n{make_tweet_main(28)}')
    except KeyboardInterrupt:
        print('\nAdios!')
