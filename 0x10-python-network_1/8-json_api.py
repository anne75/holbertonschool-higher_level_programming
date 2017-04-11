#!/usr/bin/python3
"""
This is module 8-json_api.
This module tries to read some json from a server using requests
"""
import requests
import sys


def print_json(q=""):
    """
    prints a valid json

    Arguments:
        q: a parameter for a POST request
    """
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        result = r.json()
    except ValueError as e:
        print("Not a valid JSON")
        return
    if not result:
        print("No result")
    else:
        print("[{}] {}".format(result.get('id'), result.get('name')))


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        print_json(sys.argv[1])
    else:
        print_json()
