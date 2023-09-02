#!/usr/bin/python3
"""
Script that detches https://alx-intranet.hbtn.io/status
"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(f"Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
