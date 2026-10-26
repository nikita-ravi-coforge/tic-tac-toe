# Tic-Tac-Toe Plan

## Goal

I'm building a Tic-Tac-Toe game that runs in the terminal on a 3x3 board. Two people can play each other, or one person can play as X against the computer on Easy or Hard.

## Requirements

| ID | Requirement | How I'll verify it |
|----|-------------|--------------------|
| R1 | X always goes first, and turns switch after every valid move. | Test that the game starts on X and moves to O after one move |
| R2 | A new board has 9 empty cells. | Test that `empty_cells()` returns 9 cells on a new board |
| R3 | Placing a mark on a taken cell is rejected, the original mark stays, and the player doesn't lose their turn. | Test that `place_mark` returns False and the cell still has the first mark |
| R4 | Positions off the board are rejected, including negative ones like (-1, 0). | Parametrized test with (-1, 0), (0, -1), (3, 0) and (0, 3) |
| R5 | Letters, blank input, or only one number shows a message and the same player tries again. | Play the game and type "a b", nothing, and "2" |
| R6 | The game detects a win across, down, and on both diagonals. | A test for a row, a column, and each diagonal |
| R7 | A full board with no winner counts as a draw. | Fill the board with no winner and check `is_full()` is True and `has_won()` is False for both marks |
| R8 | Easy always picks an empty cell. | Run Easy with 50 different seeds and check every move is in `empty_cells()` |
| R9 | Hard takes a winning move if it has one. | Set up a board where O can win in one move and check Hard picks that cell |
| R10 | Hard never loses on 3x3 when it plays second. | Play Hard against every possible set of X moves and check X never wins |
| R11 | `choose_move` doesn't change the board. | Compare the board before and after calling `choose_move` |
| R12 | The abstract AI class can't be created directly. | `pytest.raises(TypeError)` when calling `AIPlayer()` |

## Components

- **board.py (Board):** holds the grid and the rules for placing marks and checking for a win or a full board.
- **ai.py (AIPlayer):** the abstract base class that says every AI needs a `choose_move(board, mark)` method.
- **ai.py (EasyAI):** picks a random empty cell.
- **ai.py (HardAI):** picks the best move using minimax.
- **game.py (Game):** keeps track of whose turn it is, applies moves, and checks if the game is over.
- **main.py:** shows the menus, reads what the player types, and prints the board. It's the only file that uses `print()` or `input()`.
- **tests/:** my pytest tests.
- **.github/workflows/ci.yml:** runs the tests on every pull request and every push to main.

A Game has a Board, and in computer mode it also has an AI player. EasyAI and HardAI are both kinds of AIPlayer.

## Decisions

**1. How to store the board**

I thought about a flat list of 9 cells, a dictionary keyed by (row, col), and a list of lists. I went with a list of lists stored in `_grid` inside the Board class. It lines up with how moves are given as row and column, so I don't have to convert positions. Since it's private, I can change how it's stored later without breaking the other files.

**2. How to handle different AI levels**

One option was a single AI class with `if level == "easy"` checks. Instead I'm using an abstract base class with EasyAI and HardAI as subclasses. The game just calls `choose_move` and doesn't care which level it has, so adding a new level later means adding one class. The `abc` module also stops me from making an AI that forgets to define `choose_move`.

**3. How Hard tries out moves**

Minimax has to try a lot of moves. I could copy the board each time, or place a mark, score it, and then take it back with `remove_mark`. I chose the second option because there's no copying and the code stays simpler. The risk is forgetting to undo a move, so I have a test (R11) that checks the board isn't changed after `choose_move`.

**4. Where to convert the player's numbers**

Players type rows and columns starting from 1, but my code uses 0. I'm doing the conversion only in `main.py`, so the Board and Game always work with 0-based positions and I avoid off-by-one bugs.

## What changed

- I added a `cell(row, col)` method and a `__str__` method to Board. The tests needed a way to check one cell without touching `_grid`, and `main.py` needed a way to print the board.
- `Game.play_move` returns a short status ("ok", "invalid", "win", "draw", "over") instead of just True or False, so `main.py` knows which message to show and the game never has to print anything itself.
- I moved the `rng` setup into the AIPlayer base class so EasyAI and HardAI don't repeat it. HardAI uses it to pick between moves that are equally good.
- My first version of HardAI was more complicated than it needed to be, so I simplified it. It first checks if it can win right away, and otherwise scores each move as 1 for a win, -1 for a loss, or 0 for a draw. It still uses `remove_mark` to undo each test move, like I planned.
- The "Hard never loses" test checks every possible game X can play, like I planned. It takes a few seconds, which is slower than the other tests but still fine to run every time.