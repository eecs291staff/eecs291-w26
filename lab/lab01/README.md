# Lab 01: Stdlib Data Wrangling (CSV + JSON)

Complete each step and check it off.

## Environment Setup

- [ ] Python 3.13 is installed (`python3 --version`).
- [ ] Virtual environment created (`python3 -m venv env`).
- [ ] `pytest` installed (`pip install -r requirements.txt`).

## Sanity Test

- [ ] `python3 -m pytest` passes in `labs/lab01`.

## Git Workflow

- [ ] `git status` shows your changes.
- [ ] `git add` stages your updates.
- [ ] `git commit -m "Lab 01 sanity test"`.
- [ ] `git push` pushes to your repo.

## Overview

This lab practices CSV/JSON parsing, dict-based indexing, and basic
aggregations using only the Python standard library. The dataset is a small
WNBA-style slice aligned with Project 1.

## Learning Goals

- Parse CSV and JSON using `csv` and `json` from the stdlib.
- Normalize fields and handle missing values.
- Build index dictionaries for fast lookup.
- Group and aggregate records by player and team.

## Deliverables

- Completed functions in `lab01.py`.
- All tests passing with `python3 -m pytest`.

## Data Files

- `starter/data/players.csv`
- `starter/data/game_logs.csv`
- `starter/data/teams.json`

## Tasks

Implement each function in `lab01.py`:

1. `load_players(path)`
2. `index_players(players)`
3. `load_team_map(path)`
4. `load_game_logs(path)` (skip rows with missing stats)
5. `player_totals(logs)`
6. `team_totals(logs)`
7. `top_players_by_stat(totals, stat, n=3)`

## Rules

- Use **only** the standard library.
- Keep functions pure (no printing, no file writing).
- Skip any game log row that has missing `points`, `rebounds`, or `assists`.

## Running Tests

From `labs/lab01/`:

- `pip install -r requirements.txt`
- `python3 -m pytest`

## What to Submit

- A zip of `labs/lab01/` with all tests passing.
