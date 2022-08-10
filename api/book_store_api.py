import requests


class BookApi:
    def __init__(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_bookStore(self):
        res = self._session.get(f"{self._url}/Books", headers=self._headers)
        return res

    def post_bookStore(self, book):
        res = self._session.post(f"{self._url}/Books", data=book, headers=self._headers)
        return res
