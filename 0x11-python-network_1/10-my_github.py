#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    res = r.json()
    print(res.get('id'))
