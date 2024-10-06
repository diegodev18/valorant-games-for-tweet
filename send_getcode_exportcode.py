from pickle import dump, load
from os import path

def get_code(user_path: str):
    while True:
        if path.exists(user_path):
            with open(user_path, 'rb') as f:
                return load(f)
        else:
            print('No existe las keys de telegram!')
            export_code(
                'telegram_api.pkl', 
                input('Bot_Token: '),
                input('Chat_ID: ')
            )


def export_code(user_path: str, bot_token: str, chat_id: str):
    if path.exists(user_path):
        if input('El archivo ya existe, deseas continuar? [S/N]: ').lower() not in ['s', 'si', 'y', 'yes']:
            return
    with open(user_path, 'wb') as f:
        dump({'bot_token': bot_token, 'chat_id': chat_id}, f)
    print('Archivo creado exitosamente!')


if __name__ == '__main__':
    export_code(
        'telegram_api.pkl', 
        input('Bot_Token: '),
        input('Chat_ID: ')
    )
