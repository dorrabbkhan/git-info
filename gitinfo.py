from requests import get
from re import search

"""
Prints information about a Github repository using the Github API. Inputs
URL and parses the JSON from the Github API data of the given repository.
Depends on the regex and requests modules.
"""

url_expression = r'(https?://)?(www.)?github.com/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+'
# initialize regex expression for a github repository's URL

while True:
    input_url = input("Enter url of repo: ")
    # input URL

    if search(url_expression, input_url):
        break
        # if a match exists, break out of loop

    print("Invalid URL!\n")
    # otherwise, print invalid url message and loop again

repo_expression = r'/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+'
# expression to create url for Github API

match = search(repo_expression, input_url)
# extract the /user/repo part from the url received in input

output_url = 'https://api.github.com/repos' + match.group()
# append /user/repo to Github API's url

response = get(output_url, headers={"Accept": "application/json"})
# request the repository's JSON from the Github API

if response.status_code != 200:
    print("Error reaching the repo!")
    exit()
    # exit if the request was not successful

repo_data = response.json()
# parse the obtained JSON

print(f'\nName: {repo_data["name"]}')
print(f'Owner: {repo_data["owner"]["login"]}')
print(f'Description: {repo_data["description"]}')
print(f'Is Forked: {repo_data["fork"]}')
print(f'Size: {round(repo_data["size"]/1024, 3)} MB')
print(f'Language: {repo_data["language"]}')
# print the repository's information
