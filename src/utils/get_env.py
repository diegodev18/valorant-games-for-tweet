from os import environ

from dotenv import load_dotenv

load_dotenv()


def get_env(key) -> str:
    env_value = environ.get(key)
    if env_value:
        return env_value
    raise KeyError(f"Key \'{key}\' not found in environment variables")
