import json
import requests

from .Exceptions import *


class NaverPy:

    def __init__(self, client_id='', secret=''):
        self.client_id = client_id
        self.secret = secret
        self.headers = {
            'Accept': 'application/json',
            'X-Naver-Client-Id': self.client_id,
            'X-Naver-Client-Secret': self.secret
        }
        self._test_key()


    def _test_key(self):
        url = 'https://openapi.naver.com/v1/search/blog.json?query=test'
        return self._get(url, headers=self.headers)


    def _get(self, url, headers=None):
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            return req.json()
        elif req.status_code == 401:
            raise UnauthorizedException('API Authorizing Failed :: ' + str(req.json()['errorMessage']))
        else:
            raise RequestGetException('API Requesting(Get) Error :: error code ' + str(req.status_code))


    def _post(self, url, headers=None):
        req = requests.post(url, headers=headers)
        if req.status_code == 200:
            return req.json()
        elif req.status_code == 401:
            raise UnauthorizedException('API Authorizing Failed :: ' + str(req.json()['errorMessage']))
        else:
            raise RequestPostException('API Requesting(Post) Error :: error code' + str(req.status_code))
