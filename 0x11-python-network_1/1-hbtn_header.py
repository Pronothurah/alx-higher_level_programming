#!/usr/bin/python3
"""Fetches a header of a response from a URL."""
import urllib.request
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
