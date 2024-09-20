import pickle as pkl


def dump(key, secret):
    with open('keys.pkl', 'wb') as f:
        pkl.dump({'key': key, 'secret': secret}, f)
    return {'key': key, 'secret': secret}


def load():
    try:
        with open('keys.pkl', 'rb') as f:
            return pkl.load(f)
    except FileNotFoundError:
        print('¡La clave no existe!')
        print('Crear clave: ')
        return dump(input('Key: '), input('Secret: '))


def main():
    keys = load()
    return keys['key'], keys['secret']


if __name__ == '__main__':
    ans = input('[1] Cargar clave\n[2] Subir clave\nOpcion: ')
    if ans in ['1', 1]:
        print(load())
    elif ans in ['2', 2]:
        dump(input('Key: '), input('Secret: '))
    else:
        print('Opcion invalida')

