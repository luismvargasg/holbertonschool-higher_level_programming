#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    res = r.json()
    for i in range(10):
        print("{}: {}".format(res[i]['sha'], res[i]['commit']['author']
              ['name']))
