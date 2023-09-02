#!/usr/bin/python3
"""
Script that detches https://alx-intranet.hbtn.io/status
"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"


with urllib.request.urlopen(url) as response:
    body = response.read()
    print(f"Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
