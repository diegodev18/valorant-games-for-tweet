from os import environ
from dotenv import load_dotenv
from sys import exit


def get() -> tuple:
    load_dotenv()
    
    if 'TWITTER_KEY' in environ:
        TWITTER_KEY = environ.get('TWITTER_KEY')
    else:
        print('TWITTER_KEY no encontrado en el archivo .env')
        exit(-1)
        
    if 'TWITTER_SECRET' in environ:
        TWITTER_SECRET = environ.get('TWITTER_SECRET')
    else:
        print('TWITTER_SECRET no encontrado en el archivo .env')
        exit(-1)
        
    if 'TWITTER_ACCESS_TOKEN' in environ:
        TWITTER_ACCESS_TOKEN = environ.get('TWITTER_ACCESS_TOKEN')
    else:
        TWITTER_ACCESS_TOKEN = None
        
    if 'TWITTER_ACCESS_TOKEN_SECRET' in environ:
        TWITTER_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    else:
        TWITTER_ACCESS_TOKEN_SECRET = None
        
    return TWITTER_KEY, TWITTER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET


if __name__ == '__main__':
    print(get())

