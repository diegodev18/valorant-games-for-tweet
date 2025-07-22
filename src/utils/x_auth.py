import requests
from time import sleep
from requests_oauthlib import OAuth1Session
from get_env import get_env


def x_auth() -> OAuth1Session:
    TWITTER_KEY = get_env("TWITTER_KEY")
    TWITTER_SECRET = get_env("TWITTER_SECRET")
    TWITTER_ACCESS_TOKEN = get_env("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = get_env("TWITTER_ACCESS_TOKEN_SECRET")

    if not TWITTER_ACCESS_TOKEN or not TWITTER_ACCESS_TOKEN_SECRET:
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        oauth = OAuth1Session(TWITTER_KEY, client_secret=TWITTER_SECRET)

        while True:
            try:
                fetch_response = oauth.fetch_request_token(request_token_url)
                break
            except ValueError:
                print(
                    "There may have been an issue with the TWITTER_KEY or TWITTER_SECRET you entered."
                )
            except requests.exceptions.ConnectionError:
                print("Error de conexion\nEsperando internet\n")
            sleep(100)

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")
        print("Got OAuth token: %s" % resource_owner_key)

        # Get authorization
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)

        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            TWITTER_KEY,
            client_secret=TWITTER_SECRET,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        TWITTER_ACCESS_TOKEN = oauth_tokens["oauth_token"]
        TWITTER_ACCESS_TOKEN_SECRET = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        TWITTER_KEY,
        client_secret=TWITTER_SECRET,
        resource_owner_key=TWITTER_ACCESS_TOKEN,
        resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET,
    )

    return oauth


if __name__ == "__main__":
    pass
