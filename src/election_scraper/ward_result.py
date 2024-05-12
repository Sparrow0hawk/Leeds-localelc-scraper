from __future__ import annotations

from dataclasses import dataclass, field, asdict

from election_scraper.candidate_row import CandidateRow


@dataclass
class WardResult:
    candidate_rows: list[CandidateRow] = field(default_factory=list)

    def add_candidate_row(self, candidate_row: CandidateRow) -> None:
        self.candidate_rows.append(candidate_row)

    def _candidate_has_most_votes(self) -> CandidateRow:
        most_votes = max(row.CandidateVotes for row in self.candidate_rows)
        winner = next(row for row in self.candidate_rows if row.CandidateVotes == most_votes)
        return winner

    def find_winner(self) -> None:
        winner = self._candidate_has_most_votes()
        winner.set_winner()

    def as_dict(self) -> list[dict[str, str | int | bool]]:
        return [asdict(row) for row in self.candidate_rows]
