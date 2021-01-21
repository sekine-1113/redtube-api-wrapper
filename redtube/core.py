import json
import requests
import urllib.parse

URL = r"https://api.redtube.com/"

def output(url, params=None):
    req = requests.get(url, params=params)
    return json.loads(req.text)
