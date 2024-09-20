import pickle
from datetime import datetime


def get_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return months


def get_dates(games):
    months = get_month()
    for n in games:
        n['date'] = n['date'].split(' ')
        n['date'] = {'año': int(n['date'][2]),
                     'mes': n['date'][0],
                     'dia': int(n['date'][1].split(',')[0]),
                     'hora': int(n['date'][4].split(':')[0])}
        for month in range(len(months)):
            if n['date']['mes'] == months[month]:
                n['date']['mes'] = month + 1
        n['date'] = datetime(n['date']['año'], n['date']['mes'], n['date']['dia'], n['date']['hora'])
    return games


def get_file():
    with open('games.pkl', 'rb') as f:
        return pickle.load(f)


def main():
    games = get_file()
    get_dates(games)
    return games


if __name__ == '__main__':
    print(main())
