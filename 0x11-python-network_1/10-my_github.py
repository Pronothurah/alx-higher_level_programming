#!/usr/bin/python3
"""Prints the GitHub id of a user."""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]
        url = 'https://api.github.com/user'

        req_headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Username': username,
            'Authorization': 'token {}'.format(password),
        }
        response = requests.get(url, headers=req_headers)

        try:
            data = response.json()
            if data['login'] == username:
                print(data['id'])
            else:
                print('None')
        except Exception:
            print('None')
