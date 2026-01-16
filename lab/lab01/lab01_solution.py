"""Lab 01 stdlib data wrangling tasks."""

from collections import defaultdict
import csv
import json
from collections.abc import Iterable
from pathlib import Path

from tests.test_lab01 import test_load_game_logs


def load_players(path: Path) -> list[dict[str, str]]:
    """Load players from CSV into a list of dicts."""
    # TODO: read CSV with csv.DictReader

    with path.open() as file:
        reader = csv.DictReader(file)

        return list(reader)

        # players = []

        # for player in reader:
        #     players.append(player)


def index_players(players: Iterable[dict[str, str]]) -> dict[str, dict[str, str]]:
    """Index players by player_id."""
    # TODO: return {player_id: player_dict}

    # player_dict = {}

    # for player in players:
    #     player_id = player["player_id"]

    #     player_dict[player_id] = player

    # return player_dict

    return {player["player_id"]: player for player in players}


def load_team_map(path: Path) -> dict[str, dict[str, str]]:
    """Load teams from JSON into a dict keyed by team_id."""
    # TODO: read JSON list and index by team_id

    team_data = {}

    with path.open() as file:
        data = json.load(file)

        for team in data:
            team_id = team["team_id"]
            team_data[team_id] = team

    return team_data


STATS = ["points", "rebounds", "assists"]


def empty_stats(log: dict[str, str]) -> bool:
    for stat in STATS:
        if log[stat] == "":
            return True

    return False


def load_game_logs(path: Path) -> list[dict[str, int | str]]:
    """Load game logs from CSV, skipping rows with missing stats."""
    # TODO: parse csv, convert numeric fields to int, skip rows with blanks

    processed_logs = []
    with path.open() as file:
        reader = csv.DictReader(file)

        for log in reader:
            if empty_stats(log):
                continue

            for stat in STATS:
                log[stat] = int(log[stat])

            processed_logs.append(log)

    return processed_logs


def player_totals(logs: Iterable[dict[str, int | str]]) -> dict[str, dict[str, int]]:
    """Aggregate totals by player_id."""
    # TODO: sum points, rebounds, assists per player

    # player_id: stats
    totals = {}

    for log in logs:
        player_id = log["player_id"]

        if player_id not in totals:
            totals[player_id] = log

        else:
            player_stats = totals[player_id]

            for stat in STATS:
                player_stats[stat] += log[stat]

    return totals


def team_totals(logs: Iterable[dict[str, int | str]]) -> dict[str, dict[str, int]]:
    """Aggregate totals by team_id."""
    # TODO: sum points, rebounds, assists per team
    totals = {}

    for log in logs:
        player_id = log["team_id"]

        if player_id not in totals:
            totals[player_id] = log

        else:
            player_stats = totals[player_id]

            for stat in STATS:
                player_stats[stat] += log[stat]

    return totals


def top_players_by_stat(
    totals: dict[str, dict[str, int]],
    stat: str,
    n: int = 3,
) -> list[tuple[str, int]]:
    """Return the top N players by a chosen stat."""
    # TODO: sort by stat desc

    players: list[tuple[str, dict[str, int]]] = list(totals.items())

    def player_sorter(player: tuple[str, dict[str, int]]):
        player_id, player_stats = player
        return player_stats[stat]

    # players.sort(key=player_sorter, reverse=True)

    players.sort(key=lambda player: player[1][stat], reverse=True)

    processed_players = []

    for player_id, player_stats in players:
        processed_players.append((player_id, player_stats[stat]))

    return processed_players[:n]
