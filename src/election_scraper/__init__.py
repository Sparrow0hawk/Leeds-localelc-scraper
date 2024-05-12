import sys

from election_scraper.cli import execute
from election_scraper.fetch_page import RequestsFetchPage


def main() -> None:
    page = RequestsFetchPage()
    results_file = open("results.csv", "w")
    execute(page, results_file, sys.argv[1:])
    results_file.close()
