#!/usr/bin/python3
"""
This is module 2-post_email.
This modules makes a post request, using a mail address as data.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request("%3A".join(sys.argv[1].rsplit(":", 1)),
                                 data, method="POST")
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode('utf-8'))
