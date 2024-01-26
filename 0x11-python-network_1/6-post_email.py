#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    sys.exit()

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

response = requests.post(url, data=data)

print(response.text)
