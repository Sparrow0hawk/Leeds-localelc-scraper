from create_result_page import create_result_page, Candidate
from election_scraper.extract_candidate_rows import extract_candidate_rows


def test_extract_candidate_rows() -> None:
    candidates = [
        Candidate(name="BAGGINS Bilbo", party="The Party Tree", votes="4,123"),
        Candidate(name="SANDYMAN Ted", party="Shire First", votes="12"),
        Candidate(name="COTTON Rosie", party="Hobbit Ladies Party", votes="4,982"),
    ]
    result_page = create_result_page(
        ward="Hobbiton", electorate="10,000", turnout="80%", spoilt="102", candidate_list=candidates
    )

    results = extract_candidate_rows(result_page)
    row1, row2, row3 = results

    assert (
        row1["AreaName"] == "Hobbiton"
        and row1["Electorate"] == 10_000
        and row1["Turnout"] == "80%"
        and row1["Spoilt_ballots"] == 102
        and row1["CandidateForename"] == "Bilbo"
        and row1["CandidateSurname"] == "BAGGINS"
        and row1["CandidateVotes"] == 4123
        and row1["Elected"] is False
    )
