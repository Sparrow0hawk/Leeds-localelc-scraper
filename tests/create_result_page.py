from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def create_result_page(ward: str, electorate: str, turnout: str, spoilt: str, candidate_list: list[Candidate]) -> str:
    template_path = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("result.html.j2")

    all_candidates = [asdict(candidate) for candidate in candidate_list]

    html_page = template.render(
        {"ward": ward, "electorate": electorate, "turnout": turnout, "spoilt": spoilt, "candidates": all_candidates}
    )

    return html_page


@dataclass
class Candidate:
    name: str
    party: str
    votes: str
