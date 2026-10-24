from board import Board

class Game:

    def __init__(self):
        self._board = Board()
        self._current = "X"
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
        """The winning mark, or None if nobody has won"""
        return self._winner

    @property
    def is_over(self):
        return self._over

    def play_move(self, row, col):
        """Play the current player's move. "invalid" if the move is not allowed the turn does not change,
        "win" or "draw" if the game just ended, "over" if the game had already
        ended, "ok" if play continues with the other player.
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