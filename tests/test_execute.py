from io import StringIO

import pytest

from create_result_page import create_result_page, Candidate
from election_scraper.cli import execute
from fakes import FakeFetchPage


@pytest.fixture
def output() -> StringIO:
    return StringIO()


def test_execute(output: StringIO) -> None:
    candidates = [
        Candidate(name="BAGGINS Bilbo", party="The Party Tree", votes="4,123"),
    ]
    result_page = create_result_page(
        ward="Hobbiton", electorate="10,000", turnout="80%", spoilt="102", candidate_list=candidates
    )
    args = ["--url", "test"]
    page = FakeFetchPage(result_page)

    execute(page, output, args)

    header, line1 = output.getvalue().splitlines()

    assert (
        header
        == "AreaName,CandidateForename,CandidateSurname,CandidateDescription,CandidateVotes,Electorate,Turnout,Spoilt_ballots,Elected"
        and line1 == "Hobbiton,Bilbo,BAGGINS,The Party Tree,4123,10000,80%,102,True"
    )
