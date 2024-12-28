from os import environ
from dotenv import load_dotenv

load_dotenv()

def get(key, error = False) -> str:
    if key in environ:
        return environ.get(key)
    elif error:
        raise KeyError(f"Key {key} no encontrada en las variables de entorno :(")
    else:
        return None
    