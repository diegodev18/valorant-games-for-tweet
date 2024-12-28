from os import path
from json import load as jload
import pickle as pkl


def dump(key, secret):
    with open('twitter_keys.pkl', 'wb') as f:
        pkl.dump({'key': key, 'secret': secret}, f)
    return {'key': key, 'secret': secret}


def load():
    if path.exists('twitter_keys.json'):
        return jload(open('twitter_keys.json', 'r'))
    try:
        with open('twitter_keys.pkl', 'rb') as f:
            return pkl.load(f)
    except FileNotFoundError:
        print('¡La clave no existe!')
        print('Crear clave: ')
        return dump(input('Twitter Key: '), input('Twitter Secret: '))


def main():
    keys = load()
    return keys['key'], keys['secret']


if __name__ == '__main__':
    ans = input('[1] Cargar clave\n[2] Subir clave\nOpcion: ')
    if ans in ['1', 1]:
        print(load())
    elif ans in ['2', 2]:
        dump(input('Twitter Key: '), input('Twitter Secret: '))
    else:
        print('Opcion invalida')

