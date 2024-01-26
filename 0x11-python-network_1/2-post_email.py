#!/usr/bin/python3
"""Sends for data to a url"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
