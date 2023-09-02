#!/usr/bin/python3
"""
script that takes a url and displays value
of X-Requests-Id variable found in header response
"""
import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error fetching URL:", e)
