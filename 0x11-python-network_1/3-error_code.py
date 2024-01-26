#!/usr/bin/python3
"""Sends a request to a URL and prints its response or error code."""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                body = response.read()
                print(body.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
