import json
import requests
import urllib.parse

URL = r"https://api.redtube.com/"

def output(output_type, data):
    if output_type.lower() == "json":
        return json.loads(data)
    return data
