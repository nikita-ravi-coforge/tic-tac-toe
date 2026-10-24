import pytest

from board import Board


@pytest.fixture
def board():
    """A fresh empty board"""
    return Board()


def test_new_board_is_empty(board):
    assert len(board.empty_cells()) == 9
    assert board.is_full() is False

def test_place_mark_puts_mark_on_cell(board):
    assert board.place_mark(1, 1, "X") is True
    assert board.cell(1, 1) == "X"

def test_taken_cell_is_rejected_and_first_mark_stays(board):
    board.place_mark(0, 0, "X")
    assert board.place_mark(0, 0, "O") is False
    assert board.cell(0, 0) == "X"

@pytest.mark.parametrize("row, col", [(-1, 0), (0, -1), (-1, -1), (3, 0), (0, 3)])
def test_off_board_positions_are_rejected(board, row, col):
    assert board.place_mark(row, col, "X") is False
    assert len(board.empty_cells()) == 9

def test_remove_mark_empties_the_cell(board):
    board.place_mark(2, 1, "O")
    board.remove_mark(2, 1)
    assert (2, 1) in board.empty_cells()
    assert len(board.empty_cells()) == 9

@pytest.mark.parametrize("row", [0, 1, 2])
def test_win_across(board, row):
    for col in range(3):
        board.place_mark(row, col, "X")
    assert board.has_won("X") is True
    assert board.has_won("O") is False

@pytest.mark.parametrize("col", [0, 1, 2])
def test_win_down(board, col):
    for row in range(3):
        board.place_mark(row, col, "O")
    assert board.has_won("O") is True

def test_win_on_main_diagonal(board):
    for i in range(3):
        board.place_mark(i, i, "X")
    assert board.has_won("X") is True

def test_win_on_other_diagonal(board):
    for i in range(3):
        board.place_mark(i, 2 - i, "X")
    assert board.has_won("X") is True

def test_two_in_a_row_is_not_a_win(board):
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    assert board.has_won("X") is False

def test_full_board_with_no_winner_is_a_draw(board):
    # X | O | X
    # X | O | O
    # O | X | X
    marks = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    for row in range(3):
        for col in range(3):
            board.place_mark(row, col, marks[row][col])
    assert board.is_full() is True
    assert board.has_won("X") is False
    assert board.has_won("O") is False

def test_board_text_shows_the_marks(board):
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")
    assert str(board) == "X |   |  \n--+---+--\n  | O |  \n--+---+--\n  |   |  "