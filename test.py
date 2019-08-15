import gitinfo
import unittest
import re

"""
Testing file for git-info
Uses unittest to set up tests for possible 
inputs and expected outputs
"""

base_urls = [

    "https://github.com/dorrabbkhan/git-info",
    "http://github.com/dorrabbkhan/git-info",
    "https://www.github.com/dorrabbkhan/git-info",
    "http://www.github.com/dorrabbkhan/git-info",
    "www.github.com/dorrabbkhan/git-info",
    "github.com/dorrabbkhan/git-info"

]
# create URL's to check regex with

test_repo = gitinfo.Repository(base_urls[0])
# initialized a repository object with the first URL in base_urls

class TestRepo(unittest.TestCase):
    # create the testing class with unittest

    def test_url_regex(self):
        # test the regex of the input URL for each URL in base_urls

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.url_expression, url))

    def test_output_url_regex(self):
        # check regex of output URL for each URL in base_urls

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.repo_expression, url))

    def test_repo_object_url(self):
        # check if the new object's stored URL equals the input URL

        self.assertEqual(base_urls[0], test_repo.url)

    def test_name(self):
        # check if returned name is string

        self.assertIs(type(test_repo.name()), str)

    def test_owner(self):
        # check if returned owner name is string

        self.assertIs(type(test_repo.owner()), str)

    def test_description(self):
        # check if returned description is string

        self.assertIs(type(test_repo.description()), str)

    def test_is_forked(self):
        # check if returned is_forked is boolean

        self.assertIs(type(test_repo.is_forked()), bool)

    def test_created_at(self):
        # check if returned created at date is string

        self.assertIs(type(test_repo.created_at()), str)

    def test_size(self):
        # check if returned repository size is string

        self.assertIs(type(test_repo.size()), int)

    def test_language(self):
        # check if returned language is string

        self.assertIs(type(test_repo.language()), str)

    def test_watchers(self):
        # check if returned number of watchers is int

        self.assertIs(type(test_repo.watchers()), int)

    def test_stars(self):
        # check if returned number of stars is int

        self.assertIs(type(test_repo.stars()), int)

    def test_forks(self):
        # check if returned number of forks is int

        self.assertIs(type(test_repo.forks()), int)

    def test_open_issues(self):
        # check if returned number of open issues is int

        self.assertIs(type(test_repo.open_issues()), int)

    def test_default_branch(self):
        # check if returned number of branches is int

        self.assertIs(type(test_repo.default_branch()), str)

    def test_subscribers(self):
        # check if returned subscriber count is int

        self.assertIs(type(test_repo.subscribers()), int)

if __name__ == '__main__':
    # execute the test if this file is run as a Python script

    unittest.main()
