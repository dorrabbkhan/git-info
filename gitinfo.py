from requests import get
from re import search

"""
Prints information about a Github repository using the Github API. Inputs
URL and parses the JSON from the Github API data of the given repository.
Depends on the regex and requests modules.
"""

url_expression = r'(https?://)?(www.)?github.com/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+'
# initialize regex expression for a github repository's URL

repo_expression = r'/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+'
# expression to create url for Github API

class Repository:

    def __init__(self, url):
        self.url = url
        self.get_repo_info()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if not search(url_expression, url):
            raise ValueError("Invalid Github repo URL")
        self._url = url

    def get_repo_info(self):
        match = search(repo_expression, self.url)
        # extract the /user/repo part from the url received in input

        output_url = 'https://api.github.com/repos' + match.group()
        # append /user/repo to Github API's url

        response = get(output_url, headers={"Accept": "application/json"})
        # request the repository's JSON from the Github API

        if response.status_code != 200:
            raise RuntimeError("Error reaching the repository")
            # exit if the request was not successful

        self._repo_data = response.json()
        # parse the obtained JSON

    def name(self):
        return self._repo_data["name"]

    def owner(self):
        return self._repo_data["owner"]["login"]

    def description(self):
        return self._repo_data["description"]

    def is_forked(self):
        return self._repo_data["fork"] != "true"

    def created_at(self):
        return self._repo_data["created_at"]

    def size(self):
        return int(self._repo_data["size"])

    def language(self):
        return self._repo_data["language"]

    def watchers(self):
        return int(self._repo_data["watchers"])

    def stars(self):
        return int(self._repo_data["stargazers_count"])

    def forks(self):
        return int(self._repo_data["forks_count"])

    def open_issues(self):
        return int(self._repo_data["open_issues"])

    def default_branch(self):
        return self._repo_data["default_branch"]

    def subscribers(self):
        return self._repo_data["subscribers_count"]

if __name__ == "__main__":

    url = input("Enter a URL: ")
    new = Repository(url)

    print(f'\nName: {new.name()}')
    print(f'Owner: {new.owner()}')
    print(f'Description: {new.description()}')
    print(f'Is Forked: {new.is_forked()}')
    print(f'Created At: {new.created_at()}')
    print(f'Size: {round(new.size()/1024, 3)} MB')
    print(f'Language: {new.language()}')
    print(f'Watchers: {new.watchers()}')
    print(f'Stars: {new.stars()}')
    print(f'Forks: {new.forks()}')
    print(f'Open Issues: {new.open_issues()}')
    print(f'Default Branch: {new.default_branch()}')
    print(f'Subscribers: {new.subscribers()}')
    # print the repository's information