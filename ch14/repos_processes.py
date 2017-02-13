import requests
from multiprocessing import Process

def show_repos(user):
    r = requests.get(f'https://api.github.com/users/{user}/repos')
    for repository in r.json():
        print(user, repository['name'])

if __name__ == '__main__':
    for user in ('python', 'golang', 'scala'):
        p = Process(target=show_repos, args=(user,))
        p.start()
