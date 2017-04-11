#!/usr/bin/python3
"""
This is module 10-my_github.
This module takes in the github credentials and returns the github id.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
