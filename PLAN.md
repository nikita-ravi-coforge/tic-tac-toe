# PLAN

## Goal

- Terminal tic-tac-toe on a 3x3 board. X and O take turns, first to get 3 in a row wins, full board with no winner is a draw.
- You can play against the computer (easy or hard) or against a friend on the same keyboard.

## Requirements

| ID | Requirement | How I'll check it |
|----|-------------|-------------------|
| R1 | X always goes first and turns go X, O, X, O... | test that plays a few moves and checks whose turn it is each time |
| R2 | Can't place on a square that's already taken | place on 5 twice, second one should raise ValueError and board shouldn't change |
| R3 | Squares outside 1-9 get rejected | test 0, 10 and -1, all should raise ValueError |
| R4 | Wins are detected on all 8 lines for both X and O | parametrized test, 8 lines x 2 players = 16 cases |
| R5 | Full board with no 3 in a row counts as a draw | set up a known draw board, check result is draw and winner is None |
| R6 | Easy AI only ever picks empty squares in range | run it on 1000 random boards and check every move is legal |
| R7 | Hard AI takes the win if it can win right now | boards where hard has 2 in a row and the 3rd is open, check it picks that square |
| R8 | Hard never loses when it plays second | recursive test that tries every possible opponent move, O should never lose |
| R9 | Hard never loses when it plays first | same thing but hard is X |
| R10 | Typing something that isn't a number doesn't crash it, just asks again | monkeypatch input to give "abc" then "5", should end up placing on 5 |
| R11 | CI runs the tests on every push and fails if a test fails | check the Actions tab after pushing, and push a broken test on a branch to make sure it goes red |

## Components

- `board.py` / Board: holds the 9 squares and checks if a move is valid before placing it
- `ai.py` / AI: base class, every AI has a `choose_move(board, mark)` method
- `ai.py` / EasyAI: picks a random empty square
- `ai.py` / HardAI: uses minimax to pick the best square
- `game.py` / Game: keeps track of whose turn it is, the mode, and if someone won or it's a draw
- `main.py`: menus, prompts, printing the board. all the input/print stuff goes here
- `tests/`: pytest tests for everything in the requirements table
- `.github/workflows/ci.yml`: installs python + pytest and runs the tests on every push

## Decisions

**1. How the hard AI works**
- options: hardcoded rules, minimax, or minimax with alpha-beta
- went with: plain minimax
- why: 3x3 is small enough to search fully and minimax never loses, which R8 and R9 need

**2. Where input/output goes**
- options: let Game and Board print and read input, or keep it all in main.py
- went with: everything in main.py
- why: the other classes can be tested without faking a terminal