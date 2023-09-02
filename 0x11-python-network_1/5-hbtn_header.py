#!/usr/bin/python3
"""
script that takes URL, sends a request
to the URL, and displays the value of the
variabe X-Request-Id in the response header
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
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
