#!/usr/bin/python3
"""Prints the GitHub id of a user."""
import requests
import sys

if len(sys.argv) != 3:
    sys.exit()

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, token))

try:
    data = response.json()
    print(data.get('id', 'None'))
except ValueError:
    print('None')
