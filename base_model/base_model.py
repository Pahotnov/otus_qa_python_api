import json

import requests


class BaseService:

    def _request(self, method, url, params=None, headers=None, data=None, code=None):
        try:
            response = requests.request(method, url, params=params, headers=headers, data=json.dumps(data))
            if code is None:
                response.raise_for_status()
            else:
                assert response.status_code == code
                return response.json()
        except requests.exceptions.RequestException as re:
            return re

    def get(self, url, params=None):
        headers = {"Accept-Encoding": "*", "Connection": "keep-alive"}
        return self._request('GET', url, params=params, headers=headers, code=200)

    def post(self, url, data=None):
        headers = {'Content-Type': 'application/json', 'accept': 'application/json',
                   "Accept-Encoding": "*", "Connection": "keep-alive"}
        return self._request('POST', url, data=data, headers=headers, code=200)
