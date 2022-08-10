import requests


class AccountApi:
    def __init__(self, url="https://bookstore.toolsqa.com/Account/v1"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_login_authorized(self, login):
        res = self._session.post(f"{self._url}/Authorized", data=login, headers=self._headers)
        return res

    def post_login_account_generate_token(self, login):
        res = self._session.post(f"{self._url}/GenerateToken", data=login, headers=self._headers)
        return res

    def post_account_user(self, user):
        res = self._session.post(f"{self._url}/User", data=user, headers=self._headers)
        return res

    def delete_user(self, uid: str):
        res = self._session.delete(f"{self._url}/User/{uid}", headers=self._headers)
        return res

    def get_user(self, uid):
        res = self._session.get(f"{self._url}/User/{uid}", headers=self._headers)
        return res
