#!/usr/bin/python3
"""
This is module 4-hbtn_status.
This module sends simple get request using requests
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(r.text), r.text))
