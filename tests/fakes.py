from election_scraper.fetch_page import FetchPage


class FakeFetchPage(FetchPage):
    def __init__(self, html_page: str):
        self.html_page = html_page

    def fetch(self, url: str) -> str:
        return self.html_page
