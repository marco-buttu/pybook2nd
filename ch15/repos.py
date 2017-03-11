import requests

def show_repos(user):
    r = requests.get(f'https://api.github.com/users/{user}/repos')
    for repository in r.json():
        print(user, repository['name'])

if __name__ == '__main__':
    for user in ('python', 'golang', 'scala'):
        show_repos(user)
