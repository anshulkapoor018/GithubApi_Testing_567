#!/usr/bin/env python

"""
fetchGithubReposInfo_Test.py
The primary goal of this file is to Test our fetchGithubReposInfo Function
"""
__author__ = "Anshul Kapoor"

from unittest import mock
import unittest
from fetchGithubReposInfo import fetchRepos, number_of_commits

class TestFetchGithubRepos(unittest.TestCase):
    """ Test cases to check the results from API results"""

    @mock.patch('fetchGithubReposInfo.number_of_commits')
    def test_getHub_repo(self, mocked_request):
        mocked_request.return_value = 30
        with self.assertRaises(ValueError):
            fetchRepos("Restaurant-Ratings-Project")
        self.assertEqual(number_of_commits("anshulkapoor018", "Restaurant-Ratings-Project"), 30)


if __name__ == '__main__':
    unittest.main()
