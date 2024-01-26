#!/usr/bin/python3
"""Retrieves the last 10 commits of a repository."""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 2:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            commits = response.json()[:10]
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")

        except requests.exceptions.RequestException as e:
            print('Error:', e)
        except ValueError:
            print('Error retrieving commits.')
