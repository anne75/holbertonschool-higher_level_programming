#!/usr/bin/python3
"""
This is module 103-search_twitter.
This module tries to search on twitter
"""
import requests
import base64
import sys


def get_token(ck, cs):
    """
    retrieve token for a twitter query

    Arguments:
        ck: consumer key
        cs: consumer secret

    Returns:
       token
    """
    encoded = base64.b64encode(bytes(
        "{}:{}".format(ck, cs).encode('utf-8')))
    header = {"Authorization": "Basic " + str(encoded, encoding='utf-8'),
              "Content-Type":
              "application/x-www-form-urlencoded;charset=UTF-8"}

    r = requests.post("https://api.twitter.com/oauth2/token",
                      headers=header,
                      data={"grant_type": "client_credentials"})
    token = r.json().get("access_token")
    return (token)


if __name__ == "__main__":
    Consumer_Key = sys.argv[1]
    Consumer_Secret = sys.argv[2]

    token = get_token(Consumer_Key, Consumer_Secret)
    headers_search = {"Authorization": "Bearer " + token}

    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q': sys.argv[3], 'count': 5}
    r2 = requests.get(url, params=params, headers=headers_search)
    for e in r2.json().get("statuses"):
        print("[{}] {} by {}".format(
            e.get('id'), e.get('text'), e.get('user').get('name')))
