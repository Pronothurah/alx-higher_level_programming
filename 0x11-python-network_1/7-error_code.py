#!/usr/bin/python3
"""Sends a request to a URL and prints its response or error code."""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
