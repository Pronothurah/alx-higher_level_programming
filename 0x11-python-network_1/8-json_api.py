#!/usr/bin/python3
"""Sends a search parameter to a URL."""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) > 1 else ""

    form_data = {'q': query}

    response = requests.post(url, data=form_data)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
