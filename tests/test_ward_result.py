from election_scraper.ward_result import WardResult
from election_scraper.candidate_row import CandidateRow


def test_create() -> None:
    ward_result = WardResult()

    assert ward_result.candidate_rows == []


def test_add_candidate_row() -> None:
    ward_result = WardResult()
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

    ward_result.add_candidate_row(candidate_row)

    ward_result_row: CandidateRow
    (ward_result_row,) = ward_result.candidate_rows
    assert (
        ward_result_row.AreaName == "Hobbiton"
        and ward_result_row.CandidateForename == "Bilbo"
        and ward_result_row.CandidateSurname == "BAGGINS"
        and ward_result_row.CandidateDescription == "The Party Tree"
        and ward_result_row.CandidateVotes == 10
        and ward_result_row.Electorate == 100
        and ward_result_row.Turnout == "7%"
        and ward_result_row.Spoilt_ballots == 10
        and ward_result_row.Elected is False
    )


def test_find_winner() -> None:
    ward_result = WardResult()
    candidate_row1 = CandidateRow(
        AreaName="Hobbiton",
        CandidateForename="Bilbo",
        CandidateSurname="BAGGINS",
        CandidateDescription="The Party Tree",
        CandidateVotes=10,
        Electorate=100,
        Turnout="7%",
        Spoilt_ballots=10,
    )
    candidate_row2 = CandidateRow(
        AreaName="Hobbiton",
        CandidateForename="Ted",
        CandidateSurname="SANDYMAN",
        CandidateDescription="Shire First",
        CandidateVotes=9,
        Electorate=100,
        Turnout="7%",
        Spoilt_ballots=10,
    )

    ward_result.add_candidate_row(candidate_row1)
    ward_result.add_candidate_row(candidate_row2)

    ward_result.find_winner()

    ward_result_row1: CandidateRow
    ward_result_row2: CandidateRow
    ward_result_row1, ward_result_row2 = ward_result.candidate_rows
    assert (
        ward_result_row1.CandidateForename == "Bilbo"
        and ward_result_row1.CandidateSurname == "BAGGINS"
        and ward_result_row1.CandidateVotes == 10
        and ward_result_row1.Elected is True
    )
    assert (
        ward_result_row2.CandidateForename == "Ted"
        and ward_result_row2.CandidateSurname == "SANDYMAN"
        and ward_result_row2.CandidateVotes == 9
        and ward_result_row2.Elected is False
    )


def test_as_dict() -> None:
    ward_result = WardResult()
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

    ward_result.add_candidate_row(candidate_row)

    (ward_result_dict,) = ward_result.as_dict()

    assert (
        ward_result_dict["AreaName"] == "Hobbiton"
        and ward_result_dict["CandidateForename"] == "Bilbo"
        and ward_result_dict["CandidateSurname"] == "BAGGINS"
        and ward_result_dict["CandidateDescription"] == "The Party Tree"
        and ward_result_dict["CandidateVotes"] == 10
        and ward_result_dict["Electorate"] == 100
        and ward_result_dict["Turnout"] == "7%"
        and ward_result_dict["Spoilt_ballots"] == 10
        and ward_result_dict["Elected"] is False
    )
