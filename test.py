"""
Unittest file for git-info. Uses unittest to set up
tests for possible inputs and expected outputs. All
tests report ok. Execute the Python file to run tests
"""

import unittest
import re
import gitinfo

CORRECT_URLS = [

    "https://github.com/dorrabbkhan/git-info",
    "http://github.com/dorrabbkhan/git-info",
    "https://www.github.com/dorrabbkhan/git-info",
    "http://www.github.com/dorrabbkhan/git-info",
    "www.github.com/dorrabbkhan/git-info",
    "github.com/dorrabbkhan/git-info"

]

INCORRECT_URLS = [

    "gibberish43!%23\n\\^$&(&",
    "http://www.github.com/"
    "http://www.github.com//"

]

INCORRECT_TYPE_URLS = [

    234234,
    435.543,
    True,
    [43, 54, 34],
    ("http://", "github.com", "/dorrabbkhan/git-info"),
    ["http://", "github.com", "/dorrabbkhan/git-info"],
    {"http://", "github.com", "/dorrabbkhan/git-info"},

]
# create test data to check regex with

TEST_REPO = gitinfo.Repository(CORRECT_URLS[0])
# initialized a repository object with the first URL in CORRECT_URLS


class TestRepo(unittest.TestCase):
    """
    create the testing class with unittest
    """

    def test_correct_url_regex(self):
        """
        assert that correct URL's return a match
        """

        for url in CORRECT_URLS:
            self.assertIsNotNone(re.search(gitinfo.URL_EXPRESSION, url))

    def test_incorrect_url_regex(self):
        """
        assert that incorrect URL's don't return a match
        """

        for url in INCORRECT_URLS:
            self.assertIsNone(re.search(gitinfo.URL_EXPRESSION, url))

    def test_init_correct_url(self):
        """
        assert that correct URL's form a repository object
        """

        for url in CORRECT_URLS:
            temp_test_repo = gitinfo.repository(url)
            self.assertIs(type(temp_test_repo), gitinfo.Repository)

    def test_init_incorrect_url(self):
        """
        assert that string arguments with wrong format raise ValueError
        """

        for url in INCORRECT_URLS:
            self.assertRaises(ValueError, gitinfo.repository, url)

    def test_init_incorrect_type_url(self):
        """
        assert that arguments with wrong type raise TypeError
        """

        for url in INCORRECT_TYPE_URLS:
            self.assertRaises(TypeError, gitinfo.repository, url)

    def test_correct_output_url_regex(self):
        """
        assert that correct URL's return a match
        """

        for url in CORRECT_URLS:
            self.assertIsNotNone(re.search(gitinfo.REPO_EXPRESSION, url))

    def test_incorrect_output_url_regex(self):
        """
        assert that incorrect URL's don't return a match
        """

        for url in INCORRECT_URLS:
            self.assertIsNone(re.search(gitinfo.REPO_EXPRESSION, url))

    def test_repo_object_url(self):
        """
        assert that the new object's stored URL equals the input URL
        """

        self.assertEqual(CORRECT_URLS[0], TEST_REPO.url)

    def test_name(self):
        """
        assert that returned name is string
        """

        self.assertIs(type(TEST_REPO.name()), str)

    def test_owner(self):
        """
        assert that returned owner name is string
        """

        self.assertIs(type(TEST_REPO.owner()), str)

    def test_description(self):
        """
        assert that returned description is string
        """

        self.assertIs(type(TEST_REPO.description()), str)

    def test_is_forked(self):
        """
        assert that returned is_forked is boolean
        """

        self.assertIs(type(TEST_REPO.is_forked()), bool)

    def test_created_at(self):
        """
        assert that returned created at date is string
        """

        self.assertIs(type(TEST_REPO.created_at()), str)

    def test_size(self):
        """
        assert that returned repository size is string
        """

        self.assertIs(type(TEST_REPO.size()), int)

    def test_language(self):
        """
        assert that returned language is string
        """

        self.assertIs(type(TEST_REPO.language()), str)

    def test_watchers(self):
        """
        assert that returned number of watchers is int
        """

        self.assertIs(type(TEST_REPO.watchers()), int)

    def test_stars(self):
        """
        assert that returned number of stars is int
        """

        self.assertIs(type(TEST_REPO.stars()), int)

    def test_forks(self):
        """
        assert that returned number of forks is int
        """

        self.assertIs(type(TEST_REPO.forks()), int)

    def test_open_issues(self):
        """
        assert that returned number of open issues is int
        """

        self.assertIs(type(TEST_REPO.open_issues()), int)

    def test_default_branch(self):
        """
        assert that returned number of branches is int
        """

        self.assertIs(type(TEST_REPO.default_branch()), str)

    def test_subscribers(self):
        """
        assert that returned subscriber count is int
        """

        self.assertIs(type(TEST_REPO.subscribers()), int)


if __name__ == '__main__':
    # execute the test if this file is run as a Python script

    unittest.main()
