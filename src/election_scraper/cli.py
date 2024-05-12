import csv
from argparse import ArgumentParser
from typing import TextIO

from election_scraper.extract_candidate_rows import extract_candidate_rows
from election_scraper.fetch_page import FetchPage


def execute(fetch_page: FetchPage, output: TextIO, args: list[str]) -> None:
    parser = ArgumentParser(prog="election_scraper")
    parser.add_argument("--url", type=str, required=True, help="URL for Leeds local election results")

    attributes = parser.parse_args(args)

    html_page = fetch_page.fetch(attributes.url)

    candidate_rows = extract_candidate_rows(html_page)

    fieldnames = candidate_rows[0].keys()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(candidate_rows)
