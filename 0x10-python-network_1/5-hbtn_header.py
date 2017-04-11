#!/usr/bin/python3
"""
This is module 5-hbtn_header.
This module retrieves a reponse header using requests.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
