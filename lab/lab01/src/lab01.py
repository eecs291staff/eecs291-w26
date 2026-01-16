"""Lab 01 stdlib data wrangling tasks."""

import csv
import json
from collections.abc import Iterable
from pathlib import Path


def load_players(path: Path) -> list[dict[str, str]]:
    """Load players from CSV into a list of dicts."""
    # TODO: read CSV with csv.DictReader
    raise NotImplementedError


def index_players(players: Iterable[dict[str, str]]) -> dict[str, dict[str, str]]:
    """Index players by player_id."""
    # TODO: return {player_id: player_dict}
    raise NotImplementedError


def load_team_map(path: Path) -> dict[str, dict[str, str]]:
    """Load teams from JSON into a dict keyed by team_id."""
    # TODO: read JSON list and index by team_id
    raise NotImplementedError


def load_game_logs(path: Path) -> list[dict[str, int | str]]:
    """Load game logs from CSV, skipping rows with missing stats."""
    # TODO: parse csv, convert numeric fields to int, skip rows with blanks
    raise NotImplementedError


def player_totals(logs: Iterable[dict[str, int | str]]) -> dict[str, dict[str, int]]:
    """Aggregate totals by player_id."""
    # TODO: sum points, rebounds, assists per player
    raise NotImplementedError


def team_totals(logs: Iterable[dict[str, int | str]]) -> dict[str, dict[str, int]]:
    """Aggregate totals by team_id."""
    # TODO: sum points, rebounds, assists per team
    raise NotImplementedError


def top_players_by_stat(
    totals: dict[str, dict[str, int]],
    stat: str,
    n: int = 3,
) -> list[tuple[str, int]]:
    """Return the top N players by a chosen stat."""
    # TODO: sort by stat desc, then player_id asc for ties
    raise NotImplementedError
