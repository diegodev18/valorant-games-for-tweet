from pickle import dump, load
from os import path
from send_get_chatid import get_chatid

def get_code(user_path: str):
    while True:
        if path.exists(user_path):
            with open(user_path, 'rb') as f:
                return load(f)
        else:
            print('No existe las keys de telegram!')
            bot_info = {'bot_token': input('Bot_Token: ')}
            if input('\n(I)NGRESAR EL CHAT ID O BUSCAR (A)UTOMATICAMENTE? ').lower() == 'I':
                bot_info['chat_id'] = input('INTRODUCE EL CHAT ID: ')
            else:
                bot_info['chat_id'] = get_chatid(bot_info['bot_token'], input('INTRODUCE TU NOMBRE (ENTER PARA CONSEGUIR AUTOMATICAMENTE): '))
                if not bot_info['chat_id']:
                    print('El bot_token no existe!\n')
                    continue
            print(f"Bot_Token: {str(bot_info['bot_token'])[:5]}...\nChat_ID: {str(bot_info['chat_id'])[:3]}...")
            export_code(
                user_path,
                bot_info['bot_token'],
                bot_info['chat_id']
            )


def export_code(user_path: str, bot_token: str, chat_id: str):
    if path.exists(user_path):
        if input('El archivo ya existe, deseas continuar? [S/N]: ').lower() not in ['s', 'si', 'y', 'yes']:
            return
    with open(user_path, 'wb') as f:
        dump({'bot_token': bot_token, 'chat_id': chat_id}, f)
    print('Archivo creado exitosamente!')


if __name__ == '__main__':
    get_code('telegram_api.pkl')
