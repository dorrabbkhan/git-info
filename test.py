from gitinfo import repository

new = repository("https://github.com/dorrabbkhan/GitSizeViewer")

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

input()
