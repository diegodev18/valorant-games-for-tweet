from os import environ
from dotenv import load_dotenv

load_dotenv()


def get_env(key: str) -> str | None:
    env_value = environ.get(key)
    if env_value:
        return env_value
    return None


def get_multi_env(*keys):
    return (get_env(key) for key in keys)


if __name__ == "__main__":
    LIST, DATA = get_multi_env("LIST", "DATA")
    print(LIST, DATA)

