import random
from abc import ABC, abstractmethod


class AIPlayer(ABC):
    """Base class for every computer opponent"""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    @abstractmethod
    def choose_move(self, board, mark):
        """Return a row, col for an empty cell on the board"""


class EasyAI(AIPlayer):
    """Picks any empty cell at random."""

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())


class HardAI(AIPlayer):
    """Picks the best move using minimax"""

    def choose_move(self, board, mark):
        opponent = "O" if mark == "X" else "X"
        cells = board.empty_cells()

        # 1. If I can win right now, do it.
        for row, col in cells:
            board.place_mark(row, col, mark)
            won = board.has_won(mark)
            board.remove_mark(row, col)
            if won:
                return row, col

        # 2. Otherwise score every move with minimax and pick the best one.
        scores = []
        for row, col in cells:
            board.place_mark(row, col, mark)
            scores.append(self._minimax(board, mark, opponent))
            board.remove_mark(row, col)

        best = max(scores)
        best_moves = [cells[i] for i in range(len(cells)) if scores[i] == best]
        return self._rng.choice(best_moves)

    def _minimax(self, board, me, turn):
        """Score the board for me: 1 if I win, -1 if I lose, 0 for a draw.

        turn is the mark whose move it is next.
        """
        opponent = "O" if me == "X" else "X"
        if board.has_won(me):
            return 1
        if board.has_won(opponent):
            return -1
        if board.is_full():
            return 0

        scores = []
        for row, col in board.empty_cells():
            board.place_mark(row, col, turn)
            next_turn = opponent if turn == me else me
            scores.append(self._minimax(board, me, next_turn))
            board.remove_mark(row, col)

        if turn == me:
            return max(scores)  # my turn: pick my best result
        return min(scores)      # their turn assume they play their best