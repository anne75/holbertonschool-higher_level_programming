#!/usr/bin/python3
"""
This is module 101-starwars.
This module sends requests to swapi and retrieve results.
The argument is a string that may appear in Star Wars.
"""
import sys
import requests


if __name__ == "__main__":
    names = []
    next_page = True
    url = "http://swapi.co/api/people/"
    headers = {'search': sys.argv[1]}
    while next_page:
        a = requests.get(url, params=headers).json()
        for element in a.get('results'):
            names.append(element.get('name'))
        if a.get('next') is not None:
            url = a.get('next')
        else:
            next_page = False

    print("Number of result: {:d}".format(a.get('count')))
    if names:
        print("\n".join(names))
