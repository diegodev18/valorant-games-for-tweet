import requests
from utils.get_env import get_multi_env
from time import sleep
from requests_oauthlib import OAuth1Session
from sys import exit


def x_auth() -> OAuth1Session:
    X_KEY, X_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET = get_multi_env(
        "X_KEY", "X_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"
    )

    if not X_KEY or not X_KEY:
        print('YOU MUST HAVE "X_KEY" AND "X_KEY" IN ".ENV" FILE')
        exit(-1)

    if not X_ACCESS_TOKEN or not X_ACCESS_TOKEN_SECRET:
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        oauth = OAuth1Session(X_KEY, client_secret=X_SECRET)

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
        print(f"Got OAuth token: {resource_owner_key}")

        # Get authorization
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)

        print(f"Please go here and authorize: {authorization_url}")
        verifier = input("Paste the PIN here: ")

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            X_KEY,
            client_secret=X_SECRET,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        X_ACCESS_TOKEN = oauth_tokens["oauth_token"]
        X_ACCESS_TOKEN_SECRET = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        X_KEY,
        client_secret=X_SECRET,
        resource_owner_key=X_ACCESS_TOKEN,
        resource_owner_secret=X_ACCESS_TOKEN_SECRET,
    )

    return oauth


if __name__ == "__main__":
    x_auth()
