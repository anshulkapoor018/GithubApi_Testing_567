#!/usr/bin/env python

"""
fetchGithubReposInfo_Test.py
The primary goal of this file is to Test our fetchGithubReposInfo Function
"""
__author__ = "Anshul Kapoor"

import unittest
from fetchGithubReposInfo import fetchRepos

class TestFetchGithubRepos(unittest.TestCase):
    """ Test cases to check the results from API results"""
    def test_api_results(self):
        self.assertEqual(fetchRepos('anshulkapoor018'), ["Repo: Restaurant-Ratings-Project  Number of commits: 30"])


if __name__ == '__main__':
    unittest.main()
