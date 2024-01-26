#!/usr/bin/python3
"""Sends for data to a url"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]

        data = {'email': email}

        response = requests.post(url, data=data)

        print(response.text)
