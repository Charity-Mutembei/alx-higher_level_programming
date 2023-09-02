#!/usr/bin/python3
"""
Technical interview
"""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {
        'per_page': 10,
        'page': 1
    }

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
