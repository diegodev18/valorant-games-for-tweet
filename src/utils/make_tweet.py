from random import choice
from utils.upload_item_to_write import upload_items
from utils.get_games import get_games
from utils.get_data import get_data


def make_tweet_main(day):
    emotes = "⌚🥵🤩🪐🍫🎬🤟🤯👏🔥🚀💣🎇🔫☣️☕🌭☀️"
    # Get from files
    phrases = get_data("phrases")
    at_signs = get_data("at_signs")
    # Start function
    checked_games = get_games()
    games_today = [
        f"{choice(phrases)} {choice(['en', 'para'])} @{choice(at_signs)} {choice(emotes)}\n"
    ]
    for game in checked_games:
        games_today.append(f"{game['date']} - {game['left']} vs {game['right']}")
    upload_items(checked_games, "history.txt")
    if len(games_today) > 1:
        tweet = "\n".join(games_today)
        tweet = f"{tweet[:275]}..."
        return tweet
    return None


if __name__ == "__main__":
    from datetime import datetime

    try:
        print(f"\n{make_tweet_main(datetime.now().day + 1)}")
    except KeyboardInterrupt:
        print("\nAdios!")
