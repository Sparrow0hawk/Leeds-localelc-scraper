from election_scraper.candidate_row import CandidateRow


def test_create() -> None:
    candidate_row = CandidateRow(
        AreaName="Hobbiton",
        CandidateForename="Bilbo",
        CandidateSurname="BAGGINS",
        CandidateDescription="The Party Tree",
        CandidateVotes=10,
        Electorate=100,
        Turnout="7%",
        Spoilt_ballots=10,
    )

    assert (
        candidate_row.AreaName == "Hobbiton"
        and candidate_row.CandidateForename == "Bilbo"
        and candidate_row.CandidateSurname == "BAGGINS"
        and candidate_row.CandidateDescription == "The Party Tree"
        and candidate_row.CandidateVotes == 10
        and candidate_row.Electorate == 100
        and candidate_row.Turnout == "7%"
        and candidate_row.Spoilt_ballots == 10
        and candidate_row.Elected is False
    )


def test_set_winner() -> None:
    candidate_row = CandidateRow(
        AreaName="Hobbiton",
        CandidateForename="Bilbo",
        CandidateSurname="BAGGINS",
        CandidateDescription="The Party Tree",
        CandidateVotes=10,
        Electorate=100,
        Turnout="7%",
        Spoilt_ballots=10,
    )

    candidate_row.set_winner()

    assert candidate_row.Elected is True
