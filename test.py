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

class TestRepo(unittest.TestCase):

    def test_url_regex(self):

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.url_expression, url))

    def test_output_url_regex(self):

        for url in base_urls:
            self.assertIsNotNone(re.search(gitinfo.repo_expression, url))

if __name__ == '__main__':
    unittest.main()


# print(f'\nName: {new.name()}')
# print(f'Owner: {new.owner()}')
# print(f'Description: {new.description()}')
# print(f'Is Forked: {new.is_forked()}')
# print(f'Created At: {new.created_at()}')
# print(f'Size: {round(new.size()/1024, 3)} MB')
# print(f'Language: {new.language()}')
# print(f'Watchers: {new.watchers()}')
# print(f'Stars: {new.stars()}')
# print(f'Forks: {new.forks()}')
# print(f'Open Issues: {new.open_issues()}')
# print(f'Default Branch: {new.default_branch()}')
# print(f'Subscribers: {new.subscribers()}')
