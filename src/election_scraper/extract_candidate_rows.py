from __future__ import annotations

from bs4 import BeautifulSoup

from election_scraper.accordion import AccordionComponent


def extract_candidate_rows(html_page: str) -> list[dict[str, str | int]]:
    soup = BeautifulSoup(html_page, features="html.parser")
    accordion_tag = soup.select_one("div.accordion")
    assert accordion_tag
    accordion = AccordionComponent(accordion_tag)

    ward_result_rows = [ward_row for ward_rows in accordion.result_rows() for ward_row in ward_rows.as_dict()]

    return ward_result_rows
