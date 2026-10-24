"""The Tic-Tac-Toe board."""

EMPTY = " "
SIZE = 3


class Board:
    """A 3x3 Tic-Tac-Toe board. Rows and columns are numbered from 0."""

    def __init__(self):
        self._grid = [[EMPTY] * SIZE for _ in range(SIZE)]

    def _in_range(self, row, col):
        return 0 <= row < SIZE and 0 <= col < SIZE

    def cell(self, row, col):
        """Return the mark at row, col ("X", "O", or a space)."""
        return self._grid[row][col]

    def place_mark(self, row, col, mark):
        """Place mark at row, col Return True if placed, False if taken or off the board"""
        if not self._in_range(row, col):
            return False
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def remove_mark(self, row, col):
        """Clear the cell at row, col Used by the Hard AI to undo a test move"""
        if self._in_range(row, col):
            self._grid[row][col] = EMPTY

    def empty_cells(self):
        """Return a list of (row, col) tuples for every empty cell."""
        return [(r, c) for r in range(SIZE) for c in range(SIZE)
                if self._grid[r][c] == EMPTY]

    def _lines(self):
        """Return every row, column, and diagonal as a list of cells."""
        rows = [row[:] for row in self._grid]
        cols = [[self._grid[r][c] for r in range(SIZE)] for c in range(SIZE)]
        main_diagonal = [self._grid[i][i] for i in range(SIZE)]
        other_diagonal = [self._grid[i][SIZE - 1 - i] for i in range(SIZE)]
        return rows + cols + [main_diagonal, other_diagonal]

    def has_won(self, mark):
        """Return True if mark fills a whole row, column, or diagonal."""
        return any(all(cell == mark for cell in line) for line in self._lines())

    def is_full(self):
        """Return True if there are no empty cells left."""
        return not self.empty_cells()

    def __str__(self):
        separator = "-+-".join("-" * SIZE)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < SIZE - 1:
                lines.append(separator)
        return "\n".join(lines)