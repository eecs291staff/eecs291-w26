"""Tests for Lab 05: Hash Performance."""

from __future__ import annotations

from pathlib import Path

import pytest

import src.lab05 as lab

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def test_load_tracks_count():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    assert len(tracks) == 12


def test_load_tracks_fields():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    t = tracks[0]
    assert t["track_id"] == "t001"
    assert t["title"] == "Run"
    assert t["artist"] == "Aurora Singh"


def test_load_plays_count():
    plays = lab.load_plays(DATA_DIR / "plays.csv")
    assert len(plays) == 24


def test_load_plays_int_conversion():
    plays = lab.load_plays(DATA_DIR / "plays.csv")
    assert isinstance(plays[0]["play_count"], int)
    assert plays[0]["play_count"] == 3


# ---------------------------------------------------------------------------
# Part 1: Load factor and hashing
# ---------------------------------------------------------------------------

def test_compute_load_factor_basic():
    assert lab.compute_load_factor(40, 64) == pytest.approx(0.625)


def test_compute_load_factor_half():
    assert lab.compute_load_factor(8, 16) == pytest.approx(0.5)


def test_compute_load_factor_zero_buckets():
    with pytest.raises(ValueError):
        lab.compute_load_factor(10, 0)


def test_hash_to_bucket_in_range():
    for key in ["t001", "t002", "t003", "t004", "t005"]:
        b = lab.hash_to_bucket(key, 8)
        assert 0 <= b < 8


def test_hash_to_bucket_deterministic():
    assert lab.hash_to_bucket("t001", 16) == lab.hash_to_bucket("t001", 16)


def test_hash_to_bucket_zero_buckets():
    with pytest.raises(ValueError):
        lab.hash_to_bucket("t001", 0)


# ---------------------------------------------------------------------------
# Part 2: Chaining table
# ---------------------------------------------------------------------------

def test_build_chaining_table_length():
    table = lab.build_chaining_table(["t001", "t002", "t003"], 8)
    assert len(table) == 8


def test_build_chaining_table_all_keys_present():
    keys = ["t001", "t002", "t003", "t004", "t005"]
    table = lab.build_chaining_table(keys, 8)
    all_keys = [k for chain in table for k in chain]
    assert sorted(all_keys) == sorted(keys)


def test_build_chaining_table_empty_keys():
    table = lab.build_chaining_table([], 4)
    assert all(len(chain) == 0 for chain in table)


def test_count_collisions_no_collision():
    # 8 buckets, each with at most 1 entry → 0 collisions
    table = [[] for _ in range(8)]
    table[0] = ["t001"]
    table[1] = ["t002"]
    assert lab.count_collisions(table) == 0


def test_count_collisions_with_collision():
    table = [[] for _ in range(4)]
    table[0] = ["t001", "t003", "t007"]  # 2 collisions
    table[1] = ["t002"]                   # 0 collisions
    table[2] = ["t004", "t008"]           # 1 collision
    assert lab.count_collisions(table) == 3


def test_max_chain_length_basic():
    table = [["a", "b", "c"], ["d"], [], ["e", "f"]]
    assert lab.max_chain_length(table) == 3


def test_max_chain_length_empty():
    table = [[], [], []]
    assert lab.max_chain_length(table) == 0


def test_bucket_distribution_basic():
    table = [["a", "b"], ["c"], [], ["d", "e", "f"], []]
    dist = lab.bucket_distribution(table)
    assert dist[0] == 2
    assert dist[1] == 1
    assert dist[2] == 1
    assert dist[3] == 1


# ---------------------------------------------------------------------------
# Part 3: Simulate inserts and resize
# ---------------------------------------------------------------------------

def test_simulate_inserts_load_factor():
    keys = [f"t{i:03d}" for i in range(1, 9)]  # 8 keys
    result = lab.simulate_inserts(keys, 16)
    assert result["load_factor"] == pytest.approx(0.5)


def test_simulate_inserts_keys():
    keys = [f"t{i:03d}" for i in range(1, 13)]  # 12 keys
    result = lab.simulate_inserts(keys, 8)
    assert "load_factor" in result
    assert "collisions" in result
    assert "max_chain" in result
    assert result["load_factor"] == pytest.approx(1.5)


def test_resize_table_all_keys_preserved():
    keys = ["t001", "t002", "t003", "t004", "t005", "t006"]
    old_table = lab.build_chaining_table(keys, 4)
    new_table = lab.resize_table(old_table, 16)
    assert len(new_table) == 16
    all_keys = [k for chain in new_table for k in chain]
    assert sorted(all_keys) == sorted(keys)


def test_resize_table_fewer_collisions():
    keys = [f"t{i:03d}" for i in range(1, 13)]
    small_table = lab.build_chaining_table(keys, 4)
    large_table = lab.resize_table(small_table, 32)
    assert lab.count_collisions(large_table) <= lab.count_collisions(small_table)


# ---------------------------------------------------------------------------
# Part 4: Spotify data
# ---------------------------------------------------------------------------

def test_total_plays_by_track():
    plays = lab.load_plays(DATA_DIR / "plays.csv")
    totals = lab.total_plays_by_track(plays)
    # t001 appears in p001(3), p003(2), p006(4), p013(3) = 12
    assert totals["t001"] == 12
    # t007 appears in p010(6), p015(4), p022(7) = 17
    assert totals["t007"] == 17


def test_build_track_index_length():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    index = lab.build_track_index(tracks, 16)
    assert len(index) == 16


def test_build_track_index_all_tracks_present():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    index = lab.build_track_index(tracks, 16)
    all_ids = [t["track_id"] for chain in index for t in chain]
    assert sorted(all_ids) == sorted(t["track_id"] for t in tracks)


def test_lookup_track_found():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    index = lab.build_track_index(tracks, 16)
    result = lab.lookup_track(index, "t003", 16)
    assert result is not None
    assert result["title"] == "Midnight Drive"


def test_lookup_track_not_found():
    tracks = lab.load_tracks(DATA_DIR / "tracks.csv")
    index = lab.build_track_index(tracks, 16)
    result = lab.lookup_track(index, "t999", 16)
    assert result is None
