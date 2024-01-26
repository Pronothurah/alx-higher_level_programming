#!/usr/bin/python3
"""Retrieves the last 10 commits of a repository."""
import requests
import sys

if len(sys.argv) != 3:
    sys.exit()

repo_name = sys.argv[1]
owner_name = sys.argv[2]
url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

response = requests.get(url)

try:
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
except ValueError:
    print('Error retrieving commits.')
