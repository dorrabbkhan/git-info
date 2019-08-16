"""
Returns information about a Github repository using the Github API. Inputs
URL and parses the JSON from the Github API data of the given repository.
Depends on the regex and requests modules.
"""

from re import search
from requests import get

URL_EXPRESSION = r'(https?://)?(www.)?github.com/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+'
# initialize regex expression for a github repository's URL

REPO_EXPRESSION = r'/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+'
# expression to create url for Github API


class Repository:
    """
    create class for information of repository
    """

    def __init__(self, input_url):
        # initialize URL

        self._url = ''
        self.url = input_url
        # set the repository's URL

        self.set_repo_info()
        # obtain repository's information

    @property
    def url(self):
        """
        getter function for the URL
        """
        return self._url

    @url.setter
    def url(self, input_url):
        """
        set URL after running checks on it
        """

        if not isinstance(input_url, str):
            raise TypeError("URL parameter only accepts string")
            # raise error if type of the argument is not string

        if not search(URL_EXPRESSION, input_url):
            raise ValueError("Invalid Github repo URL")
            # raise error if the input URL does not match the regex pattern

        self._url = input_url

    def set_repo_info(self):
        """
        function to obtain the repository's information from the web
        and store it in this object
        """

        match = search(REPO_EXPRESSION, self.url)
        # extract the /user/repo part from the url received in input

        output_url = 'https://api.github.com/repos' + match.group()
        # append /user/repo to Github API's URL

        response = get(output_url, headers={"Accept": "application/json"})
        # request the repository's JSON from the Github API

        if response.status_code != 200:
            raise ConnectionError("Error reaching the repository")
            # raise error if the request was not successful

        self._repo_data = response.json()
        # parse the obtained JSON and store it

    def name(self):
        """
        return the repository's name
        """

        return self._repo_data["name"]

    def owner(self):
        """
        return the repository's owner's username
        """

        return self._repo_data["owner"]["login"]

    def description(self):
        """
        return the repository's description
        """

        return self._repo_data["description"]

    def is_forked(self):
        """
        return whether the repository is forked
        """

        return bool(self._repo_data["fork"])

    def created_at(self):
        """
        return the repository's creation date and time
        """

        return self._repo_data["created_at"]

    def size(self):
        """
        return the repository's size in KB
        """

        return self._repo_data["size"]

    def language(self):
        """
        return the repository's language
        """

        return self._repo_data["language"]

    def watchers(self):
        """
        return the repository's number of watchers
        """

        return self._repo_data["subscribers_count"]

    def stars(self):
        """
        return the repository's number of stars
        """

        return self._repo_data["stargazers_count"]

    def forks(self):
        """
        return the repository's number of forks
        """

        return self._repo_data["forks_count"]

    def open_issues(self):
        """
        return the repository's number of open issues
        """

        return self._repo_data["open_issues"]

    def default_branch(self):
        """
        return the repository's default branch name
        """

        return self._repo_data["default_branch"]

    def subscribers(self):
        """
        return the repository's number of subscribers
        """

        return self._repo_data["subscribers_count"]

def repository(input_url):
    """
    initialize repository
    """

    return Repository(input_url)

if __name__ == "__main__":
    # execute only if code is not imported

    URL = input("Enter a URL: ")
    NEW = repository(URL)
    # input URL and initialize the repository object

    print(f'\nName: {NEW.name()}')
    print(f'Owner: {NEW.owner()}')
    print(f'Description: {NEW.description()}')
    print(f'Is Forked: {NEW.is_forked()}')
    print(f'Created At: {NEW.created_at()}')
    print(f'Size: {round(NEW.size()/1024, 3)} MB')
    print(f'Language: {NEW.language()}')
    print(f'Watchers: {NEW.watchers()}')
    print(f'Stars: {NEW.stars()}')
    print(f'Forks: {NEW.forks()}')
    print(f'Open Issues: {NEW.open_issues()}')
    print(f'Default Branch: {NEW.default_branch()}')
    print(f'Subscribers: {NEW.subscribers()}')
    # print the repository's information
