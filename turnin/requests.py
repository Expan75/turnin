"""Utility implmentations to hide ugly urllib parsing"""
import json
from urllib.request import Request, urlopen


default_headers = {
   "Accept": "application/vnd.github.v3+json"
}
    

def get(url, headers=default_headers) -> dict:
    request = Request(url, method="GET", headers=headers)
    with urlopen(request) as response:
        return json.loads(response.read().decode())


def post(url, data=None, headers=default_headers) -> dict:
    headers.update({'Content-Type': 'application/json'})
    request = Request(url, method="GET", headers=headers)
    with urlopen(request) as response:
        return json.loads(response.read().decode())
