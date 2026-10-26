from board import Board


class Game:
    """Runs one game If an AI is given, the computer plays O"""

    def __init__(self, ai=None):
        self._board = Board()
        self._current = "X"
        self._ai = ai
        self._winner = None
        self._over = False

    @property
    def board(self):
        return self._board

    @property
    def current_player(self):
        return self._current

    @property
    def winner(self):
        """The winning mark, or None if nobody has won."""
        return self._winner

    @property
    def is_over(self):
        return self._over

    def play_move(self, row, col):
        """Play the current player's move.

        Returns "invalid" if the move is not allowed (the turn does not change),
        "win" or "draw" if the game just ended, "over" if the game had already
        ended, or "ok" if play continues with the other player.
        """
        if self._over:
            return "over"
        if not self._board.place_mark(row, col, self._current):
            return "invalid"
        if self._board.has_won(self._current):
            self._winner = self._current
            self._over = True
            return "win"
        if self._board.is_full():
            self._over = True
            return "draw"
        self._current = "O" if self._current == "X" else "X"
        return "ok"

    def is_computer_turn(self):
        return self._ai is not None and self._current == "O" and not self._over

    def play_computer_move(self):
        """Ask the AI for its move and play it. Returns ((row, col), status)."""
        row, col = self._ai.choose_move(self._board, self._current)
        return (row, col), self.play_move(row, col)