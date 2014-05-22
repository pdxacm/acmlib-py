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

        response = requests.get(url,
                auth=(self.username, self.password))

        return response

    def post(self, path, data):

        url = self.__create_url(path)

        response = requests.post(url, data=data,
                auth=(self.username, self.password))

        return response

    def put(self, path, data):

        url = self.__create_url(path)

        response = requests.put(url, data=data,
                auth=(self.username, self.password))

        return response

    def delete(self, path):

        url = self.__create_url(path)

        response = requests.delete(url,
                auth=(self.username, self.password))

        return response

    def __create_url(self, path):
        
        if type(path) not in (list, tuple):
            path = [path]

        path = '/'.join(map(lambda x: str(x).rstrip('/'), path))
        return urljoin(self.base_url, path)
