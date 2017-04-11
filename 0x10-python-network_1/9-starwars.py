#!/usr/bin/python3
"""
This is module 9-starwars.
This module sends requests to swapi and retrieve results.
The argument is a string that may appear in Star Wars.
This is way overkill but I thought we had to query all resources.
"""
import sys
import requests


def get_by_resource(resource, string):
    """
    fetch the information for one resource
    """
    url = "http://swapi.co/api/{}/".format(resource)
    headers = {'search': string}
    r = requests.get(url, params=headers)
    return r


if __name__ == "__main__":
    resources = ["people"]
    total_count = 0
    names = []
    for r in resources:
        a = get_by_resource(r, sys.argv[1]).json()
        total_count += a.get('count')
        for element in a.get('results'):
            names.append(element.get('name'))

    print("Number of result: {:d}".format(total_count))
    print("\n".join(names))
