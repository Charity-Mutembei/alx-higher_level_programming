#!/usr/bin/python3
"""
script that takes in a letter and sends
a POST request to URL provided with
the letter as a parameter
"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
