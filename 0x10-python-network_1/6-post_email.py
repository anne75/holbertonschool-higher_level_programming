#!/usr/bin/python3
"""
This is module 6-post_email.
This module makes a POST request using requests
"""
import sys
import requests


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
