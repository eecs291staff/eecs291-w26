# EECS 291 Winter 2026 — Student Materials

This repository is the official distribution point for EECS 291 student-facing
materials (lectures, labs, projects, and exams). You will **clone once** and
**pull updates** as new content is released during the term.

## How to use this repo

- Clone at the start of the course.
- When new materials are released, pull updates:

```sh
git pull --ff-only
```

- Do **not** push changes to this repository.
- Released files will **not** be modified after publication. If a correction is
  needed, we will add new files and announce the update.

## Quick start (Jupyter)

Download the repo:

```sh
git clone https://github.com/eecs291staff/eecs291-w26.git eecs291-w26
cd eecs291-w26
```

Create a virtual environment in the repo:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install Jupyter:

```sh
python -m pip install --upgrade pip
pip install jupyter
```

Launch Jupyter and open/create notebooks:

```sh
jupyter notebook
```

Launch Jupyter for a specific notebook:

```sh
jupyter notebook lecture/<notebook-name>.ipynb
```

## Repository layout

- `lecture/` - Lecture notes and slide decks
- `lab/` - Lab handouts, worksheets, and starter files
- `project/` - Project specs, starter files, and supporting assets
- `exam/` - Exam study guides and released materials (if applicable)

## Optional: disable pushes locally

If you want to make it impossible to push from your local clone:

```sh
git remote set-url --push origin DISABLED
```

## Support

Questions and announcements will be handled via the course communication
channels. If a new file is added, we will announce it and you should pull.
