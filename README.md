# Tic-Tac-Toe

A Tic-Tac-Toe game played in the terminal on a 3×3 grid. You can play
against another person or against the computer. Players take turns placing
X and O, and the first to get three in a row (horizontally, vertically, or
diagonally) wins. If the board fills up with no winner, the game is a draw.

## How to Run

Requires Python 3.8 or later. From the project root:

    python main.py

Pick a game mode from the menu, then enter a square number from 1 to 9
when prompted:

     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9

## How to Run the Tests

Install pytest, then run it from the project root:

    pip install pytest
    pytest

The tests live in the `tests/` folder. They also run automatically on
every push through GitHub Actions (`.github/workflows/ci.yml`).