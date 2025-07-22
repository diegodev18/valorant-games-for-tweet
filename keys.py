from get_env import get as get_env


def get() -> tuple:
    TWITTER_KEY = get_env("TWITTER_KEY", True)
    TWITTER_SECRET = get_env("TWITTER_SECRET", True)
    TWITTER_ACCESS_TOKEN = get_env("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = get_env("TWITTER_ACCESS_TOKEN_SECRET")

    return (
        TWITTER_KEY,
        TWITTER_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET,
    )


if __name__ == "__main__":
    print(get())
