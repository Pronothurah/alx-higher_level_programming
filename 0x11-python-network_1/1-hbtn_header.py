#!/usr/bin/python3
import urllib.request
import sys

if len(sys.argv) != 2:
    sys.exit()

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    request_id = headers.get('X-Request-Id')
    print(request_id)
