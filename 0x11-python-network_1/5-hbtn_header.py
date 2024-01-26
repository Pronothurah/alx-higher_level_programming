#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
