import gitinfo
import unittest
import re

"""
Unittest file for git-info. Uses unittest to set up
tests for possible inputs and expected outputs. All 
tests report ok. Execute the Python file to run tests
"""

correct_urls = [

    "https://github.com/dorrabbkhan/git-info",
    "http://github.com/dorrabbkhan/git-info",
    "https://www.github.com/dorrabbkhan/git-info",
    "http://www.github.com/dorrabbkhan/git-info",
    "www.github.com/dorrabbkhan/git-info",
    "github.com/dorrabbkhan/git-info"

]

incorrect_urls = [

    "gibberish43!%23\n\\^$&(&",
    "http://www.github.com/"
    "http://www.github.com//"

]

incorrect_type_urls = [

    234234,
    435.543,
    True,
    [43, 54, 34],
    ("http://", "github.com", "/dorrabbkhan/git-info"),
    ["http://", "github.com", "/dorrabbkhan/git-info"],
    {"http://", "github.com", "/dorrabbkhan/git-info"},

]
# create URL's to check regex with

test_repo = gitinfo.Repository(correct_urls[0])
# initialized a repository object with the first URL in correct_urls

class TestRepo(unittest.TestCase):
    # create the testing class with unittest

    def test_url_regex(self):
        # test the regex of the input URL for each URL in correct_urls

        for url in correct_urls:
            self.assertIsNotNone(re.search(gitinfo.url_expression, url))
        # assert that correct URL's return a match

        for url in incorrect_urls:
            self.assertIsNone(re.search(gitinfo.url_expression, url))
        # assert that incorrect URL's don't return a match

    def test_init_method(self):
        # test the init method of the Repository class for various arguments

        for url in correct_urls:
            temp_test_repo = gitinfo.repository(url)
            self.assertIs(type(temp_test_repo), gitinfo.Repository)
            # assert that correct URL's form a repository object
        
        for url in incorrect_urls:
            self.assertRaises(ValueError, gitinfo.repository, url)
            # assert that string arguments with wrong format raise ValueError 

        for url in incorrect_type_urls:
            self.assertRaises(TypeError, gitinfo.repository, url)
            # assert that arguments with wrong type raise TypeError

    def test_output_url_regex(self):
        # check regex of output URL for each URL in correct_urls

        for url in correct_urls:
            self.assertIsNotNone(re.search(gitinfo.repo_expression, url))
            # assert that correct URL's return a match

        for url in incorrect_urls:
            self.assertIsNone(re.search(gitinfo.repo_expression, url))
            # assest that incorrect URL's don't return a match

    def test_repo_object_url(self):
        # assert that the new object's stored URL equals the input URL

        self.assertEqual(correct_urls[0], test_repo.url)

    def test_name(self):
        # assert that returned name is string

        self.assertIs(type(test_repo.name()), str)

    def test_owner(self):
        # assert that returned owner name is string

        self.assertIs(type(test_repo.owner()), str)

    def test_description(self):
        # assert that returned description is string

        self.assertIs(type(test_repo.description()), str)

    def test_is_forked(self):
        # assert that returned is_forked is boolean

        self.assertIs(type(test_repo.is_forked()), bool)

    def test_created_at(self):
        # assert that returned created at date is string

        self.assertIs(type(test_repo.created_at()), str)

    def test_size(self):
        # assert that returned repository size is string

        self.assertIs(type(test_repo.size()), int)

    def test_language(self):
        # assert that returned language is string

        self.assertIs(type(test_repo.language()), str)

    def test_watchers(self):
        # assert that returned number of watchers is int

        self.assertIs(type(test_repo.watchers()), int)

    def test_stars(self):
        # assert that returned number of stars is int

        self.assertIs(type(test_repo.stars()), int)

    def test_forks(self):
        # assert that returned number of forks is int

        self.assertIs(type(test_repo.forks()), int)

    def test_open_issues(self):
        # assert that returned number of open issues is int

        self.assertIs(type(test_repo.open_issues()), int)

    def test_default_branch(self):
        # assert that returned number of branches is int

        self.assertIs(type(test_repo.default_branch()), str)

    def test_subscribers(self):
        # assert that returned subscriber count is int

        self.assertIs(type(test_repo.subscribers()), int)

if __name__ == '__main__':
    # execute the test if this file is run as a Python script

    unittest.main()
