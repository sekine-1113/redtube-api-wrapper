import requests


URL = r"https://api.redtube.com/"

def output(url, params=None):
    req: requests.Response = requests.get(url, params=params)
    return req.json()
