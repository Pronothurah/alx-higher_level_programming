#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

url = sys.argv[1]

response = requests.get(url)

request_id = response.headers.get('X-Request-Id')

if request_id is not None:
    print(request_id)
