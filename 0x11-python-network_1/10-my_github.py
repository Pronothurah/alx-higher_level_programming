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
            'Authorization': 'token {}'.format(token),
        }
        response = requests.get(url, headers=req_headers)

        if response.status_code == 200:
            user = response.json()
            if user['login'] == username:
                print(user['id'])
            else:
                print('None')
        else:
            print('None')
