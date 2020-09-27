#!/usr/bin/env python

"""
fetchGithubReposInfo.py
The primary goal of this file is to demonstrate the fetch request to Github API's
"""
__author__ = "Anshul Kapoor"

import requests
import json


def fetchRepos(user_id):
    """ Fetch user's repositories and commits"""
    repo_api = "https://api.github.com/users/"
    commit_api = "https://api.github.com/repos/"
    fetch_url = repo_api + user_id + '/repos'
    output = []
    get_url = requests.get(fetch_url)
    repo_list = get_url.json()

    try:
        for line in repo_list:
            repo = line.get('name')
            output.append(repo)
    except (TypeError, KeyError, IndexError, AttributeError):
        raise ValueError('Not able to Fetch repositories from Entered User ID')

    return output

def number_of_commits(user_name, repo_name):
    """ to get the number of commits in a repository """
    get_url = requests.get('https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name))
    commits = get_url.json()

    if commits == 0:
        print('The respective repositories has no commits!')

    return len(commits)

def main():
    """ Get user's Github ID as input """
    user_name = input("Please enter the GitHub user ID: ")

    for repo in fetchRepos(user_name):
        num = number_of_commits(user_name, repo)
        print(f"Repo: {repo} Number of commits: {num}")


if __name__ == '__main__':
    main()
