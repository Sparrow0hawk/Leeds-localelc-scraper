from __future__ import annotations

from bs4 import BeautifulSoup
from dataclasses import asdict

from election_scraper.accordion import AccordionComponent


def extract_candidate_rows(html_page: str) -> list[dict[str, str | int]]:
    soup = BeautifulSoup(html_page, features="html.parser")
    accordion_tag = soup.select_one("div.accordion")
    assert accordion_tag
    accordion = AccordionComponent(accordion_tag)

    candidate_rows = list(accordion.result_rows())

    return [asdict(candidate_row) for candidate_row in candidate_rows]
