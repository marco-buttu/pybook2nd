import requests

def io_bound_task():
    requests.get('https://github.com/python/peps/')
