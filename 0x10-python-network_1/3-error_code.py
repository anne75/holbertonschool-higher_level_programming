#!/usr/bin/python3
"""
This is module 3-error_code.
This module makes a request using urllib and handles HTTPError
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen("%3A".join(sys.argv[1].rsplit(":", 1))) \
             as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
