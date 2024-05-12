import requests


class FetchPage:
    def fetch(self, url: str) -> str:
        raise NotImplementedError()


class RequestsFetchPage(FetchPage):
    def fetch(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
