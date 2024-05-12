from __future__ import annotations

from typing import Generator

from bs4 import Tag

from election_scraper.candidate_row import CandidateRow
from election_scraper.ward_result import WardResult


class AccordionComponent:
    def __init__(self, accordion: Tag):
        self.accordion = accordion
        self.wards = [
            AccordionHeadingComponent(row_heading) for row_heading in accordion.select("h3.accordion__heading")
        ]
        self.results = [AccordionPanelComponent(panel) for panel in accordion.select("div.accordion__panel")]

    def result_rows(self) -> Generator[WardResult, None, None]:
        result: AccordionPanelComponent
        for ward, result in zip(self.wards, self.results):
            ward_row = WardResult()
            for row in result.results_table:
                surname, forename = row.candidate_name.split(" ", maxsplit=1)
                ward_row.add_candidate_row(
                    CandidateRow(
                        AreaName=ward.ward,
                        CandidateForename=forename,
                        CandidateSurname=surname,
                        CandidateDescription=row.candidate_description,
                        CandidateVotes=int(row.candidate_votes.replace(",", "")),
                        Electorate=int(result.turnout_table.electorate.value.replace(",", "")),
                        Turnout=result.turnout_table.turnout.value,
                        Spoilt_ballots=int(result.turnout_table.spoilt_ballots.value),
                    )
                )
            ward_row.find_winner()
            yield ward_row


class AccordionHeadingComponent:
    def __init__(self, accordion_heading: Tag):
        self.ward = (accordion_heading.string or "").strip()


class AccordionPanelComponent:
    def __init__(self, accordion_panel: Tag):
        self.accordion_panel = accordion_panel
        tables = accordion_panel.select("div.table-responsive")
        self.results_table = ResultsTableComponent(tables[0])
        self.turnout_table = TurnoutTableComponent(tables[1])


class ResultsTableComponent:
    def __init__(self, results_table: Tag):
        self._rows = results_table.select("tbody tr")

    def __iter__(self) -> Generator[ResultsTableRowComponent, None, None]:
        return (ResultsTableRowComponent(row) for row in self._rows)


class ResultsTableRowComponent:
    def __init__(self, row: Tag):
        cells = row.select("td")
        candidate_name = cells[0].string
        assert candidate_name
        self.candidate_name = candidate_name.strip()
        candidate_description = cells[1].string
        assert candidate_description
        self.candidate_description = candidate_description.strip()
        candidate_votes = cells[2].string
        assert candidate_votes
        self.candidate_votes = candidate_votes.strip()


class TurnoutTableComponent:
    def __init__(self, turnout_table: Tag):
        rows = turnout_table.select("tbody tr")
        self.electorate = TurnoutTableDataComponent(rows[0])
        self.turnout = TurnoutTableDataComponent(rows[1])
        self.spoilt_ballots = TurnoutTableDataComponent(rows[2])


class TurnoutTableDataComponent:
    def __init__(self, row: Tag):
        cell = row.select_one("td")
        assert cell
        self.value = (cell.string or "").strip()
