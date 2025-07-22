import pickle
import requests
from re import findall, search
from bs4 import BeautifulSoup
from get_dates import get_dates


def scrape_games():
    games = []
    num_games = 20

    url = "https://liquipedia.net/valorant/Liquipedia:Matches"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    games_found = soup.find_all(
        class_="match-info"
    )
    n = 0
    for game in games_found:
        html_game = str(game)
        teams = findall(r'<a href="/valorant/[^"]+" title="[^"]+">([A-Z]{2,5})</a>', html_game)
        times = search(r'>([A-Za-z]+\s\d{1,2},\s\d{4}\s-\s\d{2}:\d{2})\s*<abbr', html_game)
        server = search(r'<span class="tournament-name"><a [^>]+>([^<]+)</a>', html_game)
        if len(teams) > 1 and times and server:
            list_teams = {
                "left": teams[0],
                "right": teams[1],
                "date": times.group(1),
                "server": server.group(1),
            }
            games.append(list_teams)
            n += 1
        if n == num_games:
            break
    with open("games.pkl", "wb") as f:
        pickle.dump(games, f)
    return get_dates(games)


def get_games():
    print("Obteniendo Games... ")
    games = scrape_games()
    print("Games obtenidos: ", len(games))
    return games


if __name__ == "__main__":
    from datetime import datetime
    from get_data import get_data

    games = get_games()
    tournaments = get_data("tournaments")
    for game in games:
        if game["date"].day == datetime.now().day:
            for tournament in tournaments:
                if tournament in game["server"]:
                    print(game)
                    break
