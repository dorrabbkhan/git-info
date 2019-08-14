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
    # create class for information of repository

    def __init__(self, url):
        # initialize URL

        self.url = url
        # set the repository's URL

        self.set_repo_info()
        # obtain repository's information

    @property
    def url(self):
        # getter function for the URL
        return self._url

    @url.setter
    def url(self, url):
        # set URL after running regex test on it

        if not search(url_expression, url):
            raise ValueError("Invalid Github repo URL")
            # raise error if the input URL does not match the regex pattern

        self._url = url
        # set url

    def set_repo_info(self):
        # function to obtain the repository's information from the web
        # and store it in this object

        match = search(repo_expression, self.url)
        # extract the /user/repo part from the url received in input

        output_url = 'https://api.github.com/repos' + match.group()
        # append /user/repo to Github API's URL

        response = get(output_url, headers={"Accept": "application/json"})
        # request the repository's JSON from the Github API

        if response.status_code != 200:
            raise RuntimeError("Error reaching the repository")
            # raise error if the request was not successful

        self._repo_data = response.json()
        # parse the obtained JSON and store it

    def name(self):
        # return the repository's name

        return self._repo_data["name"]

    def owner(self):
        # return the repository's owner's username

        return self._repo_data["owner"]["login"]

    def description(self):
        # return the repository's description

        return self._repo_data["description"]

    def is_forked(self):
        # return whether the repository is forked

        return self._repo_data["fork"] != "true"

    def created_at(self):
        # return the repository's creation date and time

        return self._repo_data["created_at"]

    def size(self):
        # return the repository's size in KB

        return int(self._repo_data["size"])

    def language(self):
        # return the repository's language

        return self._repo_data["language"]

    def watchers(self):
        # return the repository's number of watchers

        return int(self._repo_data["watchers"])

    def stars(self):
        # return the repository's number of stars

        return int(self._repo_data["stargazers_count"])

    def forks(self):
        # return the repository's number of forks

        return int(self._repo_data["forks_count"])

    def open_issues(self):
        # return the repository's number of open issues

        return int(self._repo_data["open_issues"])

    def default_branch(self):
        # return the repository's default branch name

        return self._repo_data["default_branch"]

    def subscribers(self):
        # return the repository's number of subscribers

        return self._repo_data["subscribers_count"]

def repository(url):
    return Repository(url)

if __name__ == "__main__":
    # execute only if code is not imported

    url = input("Enter a URL: ")
    new = repository(url)
    # input URL and initialize the repository object

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
