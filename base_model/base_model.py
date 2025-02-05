import json

import requests


class BaseService:

    def _request(self, method, url, params=None, headers=None, data=None):
        response = requests.request(method, url, params=params, headers=headers, data=json.dumps(data))
        return response.json()

    def get(self, url, params=None):
        headers = {"Accept-Encoding": "*", "Connection": "keep-alive"}
        return self._request('GET', url, params=params, headers=headers)

    def post(self, url, data=None):
        headers = {'Content-Type': 'application/json', 'accept': 'application/json',
                   "Accept-Encoding": "*", "Connection": "keep-alive"}
        return self._request('POST', url, data=data, headers=headers)
