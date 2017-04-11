#!/usr/bin/python3
"""
This is module 100-github_commits.
List 10 commits on a github repository which name and owner are passed
on the command line.
"""
import sys
import requests


if __name__ == "__main__":
    i = 0
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url).json()
    for i, result in enumerate(r):
        if i < 10:
            print("{}: {}".format(
                result.get('sha'),
                result.get('commit').get('author').get('name')))
        else:
            break
