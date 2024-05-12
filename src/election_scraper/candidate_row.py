from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CandidateRow:
    AreaName: str
    CandidateForename: str
    CandidateSurname: str
    CandidateDescription: str
    CandidateVotes: int
    Electorate: int
    Turnout: str
    Spoilt_ballots: int
