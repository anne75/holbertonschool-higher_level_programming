#!/usr/bin/python3
"""
This is module 7-error_code.
This module handles a http status code >= 400 (error) with requests
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
