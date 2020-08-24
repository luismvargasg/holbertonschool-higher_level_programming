#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
import requests
import sys
import json


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ""}
    r = requests.post(url, letter)
    try:
        res = r.json()
        if len(res) >= 0:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
