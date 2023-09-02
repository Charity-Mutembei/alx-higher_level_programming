#!/usr/bin/python3
"""
script that takes URL and an email,
sends a POST request to the URL with the email
as a parameter and displays the body of the
response decoded in utf-8
"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error sending POST request:", e)
