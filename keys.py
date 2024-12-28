from os import path
from json import load as jload
import pickle as pkl


def dump(key, secret, access_token = None, access_token_secret = None):
    with open('twitter_keys.pkl', 'wb') as f:
        pkl.dump({'key': key, 'secret': secret}, f)
    return {'key': key, 'secret': secret, 'access_token': access_token, 'access_token_secret': access_token_secret}


def load():
    if path.exists('twitter_keys.json'):
        return jload(open('twitter_keys.json', 'r'))
    try:
        with open('twitter_keys.pkl', 'rb') as f:
            return pkl.load(f)
    except FileNotFoundError:
        print('¡La clave no existe!')
        print('Crear clave: ')
        return dump(input('Api Key: '), input('Secret: '), input('Access Token: '), input('Access token secret: '))


def main():
    keys = load()
    return keys['key'], keys['secret'], keys['access_token'], keys['access_token_secret']


if __name__ == '__main__':
    ans = input('[1] Cargar clave\n[2] Subir clave\nOpcion: ')
    if ans in ['1', 1]:
        print(load())
    elif ans in ['2', 2]:
        dump(input('Twitter Key: '), input('Twitter Secret: '), input('Access Token: '), input('Access Token Secret: '))
    else:
        print('Opcion invalida')

