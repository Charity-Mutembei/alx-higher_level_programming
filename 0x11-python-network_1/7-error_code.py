#!/usr/bin/python3
"""
script that takes in a URL, sends a
request to the URL and dislays the body
of the response
"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            print("Error code:", e.response.status_code)
        else:
            print("Error:", e)
