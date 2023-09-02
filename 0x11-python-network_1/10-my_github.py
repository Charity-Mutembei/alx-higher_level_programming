#!/usr/bin/python3
"""
accessing my github
"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            data = response.json()
            print(data['id'])
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
