from requests_oauthlib import OAuth1Session
from time import sleep
from get_tw_code import get_tw_code_main
import requests
import keys


def get_api_main():
    consumer_key, consumer_secret = keys.main()

    # Get request token
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    while True:
        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
            break
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )
        except requests.exceptions.ConnectionError:
            print('Error de conexion\nEsperando internet\n')
        sleep(100)

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)

    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    """
    ans = input('[A]UTOMATICO O [M]ANUAL: ').lower()
    verifier = None
    if ans == 'm':
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")
    elif ans == 'a':
        verifier = get_tw_code_main(authorization_url, input('User: '), input('Password: '))
    if not verifier:
        exit()
    """

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    return oauth


if __name__ == '__main__':
    pass

