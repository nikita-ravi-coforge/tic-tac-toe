# Tic-Tac-Toe

A Tic-Tac-Toe game that runs in the terminal on a 3x3 board. You can play against a friend, or play as X against the computer on Easy (random moves) or Hard (uses minimax and never loses when it plays second).

## How to run the game

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Pick a mode from the menu, then enter each move as a row and a column from 1 to 3, for example `2 3`.

## How to run the tests

With the virtual environment active, run:

```bash
pytest
```

Use `pytest -v` to see each test by name. The tests also run automatically on every pull request through GitHub Actions.

## Files

- `board.py`: the Board class
- `ai.py`: the AI classes (AIPlayer, EasyAI, HardAI)
- `game.py`: turns and win or draw checks
- `main.py`: menus, prompts, and printing
- `tests/`: pytest tests
- `PLAN.md`: my plan for the project