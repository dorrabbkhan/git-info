import gitinfo
import unittest
import re

base_urls = [

    "https://github.com/dorrabbkhan/git-info",
    "http://github.com/dorrabbkhan/git-info",
    "https://www.github.com/dorrabbkhan/git-info",
    "http://www.github.com/dorrabbkhan/git-info",
    "www.github.com/dorrabbkhan/git-info",
    "github.com/dorrabbkhan/git-info"

]

test_repo = gitinfo.Repository(base_urls[0])

class TestRepo(unittest.TestCase):

    def test_url_regex(self):

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.url_expression, url))

    def test_output_url_regex(self):

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.repo_expression, url))

    def test_repo_object_url(self):

        self.assertEqual(base_urls[0], test_repo.url)

    def test_name(self):

        self.assertIsInstance(test_repo.name(), str)

    def test_owner(self):

        self.assertIsInstance(test_repo.owner(), str)

    def test_description(self):

        self.assertIsInstance(test_repo.description(), str)

    def test_is_forked(self):

        self.assertIsInstance(test_repo.is_forked(), bool)

    def test_created_at(self):

        self.assertIsInstance(test_repo.created_at(), str)

    def test_size(self):

        self.assertIsInstance(test_repo.size(), str)

if __name__ == '__main__':
    unittest.main()
