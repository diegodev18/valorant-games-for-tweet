import pickle
from re import findall

import requests
from bs4 import BeautifulSoup

from get_dates import get_dates
from get_files import get_file


def get_online_games():
    games = []
    num_games = 20

    url = "https://liquipedia.net/valorant/Liquipedia:Matches"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    games_found = soup.find_all(
        class_="wikitable wikitable-striped infobox_matches_content"
    )
    n = 0
    for game in games_found:
        teams = findall(r'data-highlightingclass="([^"]+)"', str(game))
        times = findall(r'">([^"]+) <a', str(game))
        server = game.find_all(class_="tournament-text-flex")[0]
        if len(teams) > 1:
            list_teams = {
                "left": teams[0],
                "right": teams[1],
                "date": times[0],
                "server": findall(r'">([^"]+)</a', str(server))[0],
            }
            games.append(list_teams)
            n += 1
        if n == num_games:
            break
    with open("games.pkl", "wb") as f:
        pickle.dump(games, f)
    return get_dates(games)


def main():
    print("Obteniendo Games... ")
    games = get_online_games()
    print("Games obtenidos: ", len(games))
    return games


if __name__ == "__main__":
    from datetime import datetime

    games = main()
    tournaments = get_file("tournaments.txt")
    for game in games:
        if game["date"].day == datetime.now().day:
            for tournament in tournaments:
                if tournament in game["server"]:
                    print(game)
                    break
