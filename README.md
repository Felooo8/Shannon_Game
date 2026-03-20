# Shannon Game

A small desktop implementation of the Shannon switching game (Gale variant) built with Python and Pygame.

The codebase combines a playable local GUI, a simple heuristic AI, and unit tests around the board and path-finding logic. The documentation focuses on how the game works, how to run it locally, and where the core implementation lives.

## What this repository contains

- A playable local Pygame application.
- Two computer opponents:
  - **Easy**: random legal move selection.
  - **Hard**: a shortest-path style heuristic based on the current winning roads.
- Tests for board generation, win detection, AI behavior, and game flow helpers.
- Pre-generated API/user documentation under `docs/`.

## Tech stack

- Python 3.10+
- Pygame
- Pytest

## Installation

### Option 1: minimal runtime install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Option 2: development install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Notes:
- `pygame` is the only required runtime dependency.
- The optional `names` package is supported, but no longer required; the AI falls back to built-in names if it is unavailable.

## Running the game

From the repository root, either of these works:

```bash
python run.py
```

```bash
python -m the_game
```

## How to play

1. Start the game and choose a player name.
2. Select a board size: `5x5`, `7x7`, or `9x9`.
3. Select the AI level: `Easy` or `Hard`.
4. Click an empty space to place your move.
5. After a completed game, choose either a rematch or a new game with different settings.

## Project structure

```text
assets/     Image/font assets used by the Pygame UI
docs/       Generated documentation and user guide
tests/      Unit tests for board, AI, algorithms, and game flow
the_game/   Core package: GUI, board model, AI, and game loop
run.py      Thin entrypoint for launching the application
```

## Implementation notes

- `the_game/board.py` builds the alternating starting layout used by the game board.
- `the_game/algorythms.py` contains win detection and path enumeration used by the harder AI.
- `the_game/AI.py` intentionally keeps the AI logic simple and readable rather than highly optimized.
- `the_game/GUI.py` now resolves assets relative to the repository so the game can be launched from outside the project root as well.

## Running tests

```bash
pytest
```

## Limitations

- The project is designed as a local desktop game, not a packaged cross-platform release.
- The harder AI is heuristic-based rather than exhaustive or tournament-strength.
- The public module name `algorythms.py` retains the original spelling for compatibility with the existing code and tests.

## Additional documentation

See the generated documentation in `docs/`, including `docs/Shannon_Game_User_Guide.pdf`.
