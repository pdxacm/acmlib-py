import requests

try:
    from urlparse import urljoin, urlparse, urlunparse
except ImportError:
    from urllib.parse import urljoin, urlparse, urlunparse

class Requester(object):

    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password 
        self.base_url = base_url

    def get(self, path):

        url = self.__create_url(path)

        return self.__check(requests.get(url,
                auth=(self.username, self.password)))

    def post(self, path, data):

        url = self.__create_url(path)

        return  self.__check(requests.post(url, data=data,
                auth=(self.username, self.password)))

    def put(self, path, data):

        url = self.__create_url(path)

        return self.__check(requests.put(url, data=data,
                auth=(self.username, self.password)))

    def delete(self, path):

        url = self.__create_url(path)

        return self.__check(requests.delete(url,
                auth=(self.username, self.password)))

    def __create_url(self, path):
        
        if type(path) not in (list, tuple):
            path = [path]

        path = '/'.join(map(lambda x: str(x).rstrip('/'), path))
        return urljoin(self.base_url, path)

    def __check(self, response):

        json = response.json()

        if 'exception' in json:

            exception = {
                    'TypeError':TypeError,
                    'LookupError':LookupError,
                    'ValidationError':TypeError,
                    'ValueError':ValueError,
                }[json['exception']]

            raise exception(json['message'])

        else:
            return response
