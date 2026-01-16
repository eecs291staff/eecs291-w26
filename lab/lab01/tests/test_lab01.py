from pathlib import Path

import src.lab01 as lab01

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def test_load_players():
    players = lab01.load_players(DATA_DIR / "players.csv")
    assert len(players) == 5
    assert players[0]["player_id"] == "p1"
    assert players[0]["player_name"] == "Alyssa Gray"


def test_index_players():
    players = lab01.load_players(DATA_DIR / "players.csv")
    index = lab01.index_players(players)
    assert index["p3"]["team_id"] == "PHX"


def test_load_team_map():
    teams = lab01.load_team_map(DATA_DIR / "teams.json")
    assert teams["SEA"]["team_name"] == "Seattle Storm"


def test_load_game_logs():
    logs = lab01.load_game_logs(DATA_DIR / "game_logs.csv")
    assert len(logs) == 9
    assert logs[0]["points"] == 12


def test_player_totals():
    logs = lab01.load_game_logs(DATA_DIR / "game_logs.csv")
    totals = lab01.player_totals(logs)
    assert totals["p1"]["points"] == 32
    assert totals["p4"]["assists"] == 2


def test_team_totals():
    logs = lab01.load_game_logs(DATA_DIR / "game_logs.csv")
    totals = lab01.team_totals(logs)
    assert totals["SEA"]["points"] == 40
    assert totals["NY"]["rebounds"] == 10


def test_top_players_by_stat():
    logs = lab01.load_game_logs(DATA_DIR / "game_logs.csv")
    totals = lab01.player_totals(logs)
    leaders = lab01.top_players_by_stat(totals, "points", n=3)
    assert leaders == [("p1", 32), ("p3", 25), ("p5", 17)]
