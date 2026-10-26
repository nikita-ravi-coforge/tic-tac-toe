import random

import pytest

from ai import AIPlayer, EasyAI, HardAI
from board import Board


def test_ai_player_cannot_be_created_directly():
    with pytest.raises(TypeError):
        AIPlayer(random.Random(1))


@pytest.mark.parametrize("ai", [EasyAI(random.Random(1)), HardAI(random.Random(1))])
def test_every_ai_returns_a_legal_move(ai):
    board = Board()
    board.place_mark(1, 1, "X")
    row, col = ai.choose_move(board, "O")
    assert board.place_mark(row, col, "O") is True


def test_easy_always_returns_an_empty_cell():
    board = Board()
    for row, col in [(0, 0), (0, 1), (1, 1), (2, 2)]:
        board.place_mark(row, col, "X")
    for seed in range(50):
        move = EasyAI(random.Random(seed)).choose_move(board, "O")
        assert move in board.empty_cells()


def test_easy_with_same_seed_makes_same_choice():
    board = Board()
    first = EasyAI(random.Random(7)).choose_move(board, "O")
    second = EasyAI(random.Random(7)).choose_move(board, "O")
    assert first == second


def test_easy_picks_different_cells_with_different_seeds():
    board = Board()
    moves = {EasyAI(random.Random(seed)).choose_move(board, "O") for seed in range(20)}
    assert len(moves) > 1


def test_hard_takes_a_winning_move():
 
    board = Board()
    for row, col in [(1, 0), (1, 1), (2, 0)]:
        board.place_mark(row, col, "X")
    for row, col in [(0, 0), (0, 1)]:
        board.place_mark(row, col, "O")
    assert HardAI(random.Random(1)).choose_move(board, "O") == (0, 2)


def test_hard_blocks_the_other_players_win():
    # X is about to win at (0, 2), so O must block it.
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 1, "O")
    assert HardAI(random.Random(1)).choose_move(board, "O") == (0, 2)


@pytest.mark.parametrize("ai", [EasyAI(random.Random(3)), HardAI(random.Random(3))])
def test_choose_move_leaves_board_unchanged(ai):
    board = Board()
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "O")
    board.place_mark(2, 2, "X")
    before = str(board)
    ai.choose_move(board, "O")
    assert str(board) == before
    assert len(board.empty_cells()) == 6


def x_can_beat(board, hard):
    """Try every X move from here, with Hard answering as O. True if X ever wins."""
    for row, col in board.empty_cells():
        board.place_mark(row, col, "X")
        if board.has_won("X"):
            board.remove_mark(row, col)
            return True
        if not board.is_full():
            o_row, o_col = hard.choose_move(board, "O")
            board.place_mark(o_row, o_col, "O")
            x_won = not board.has_won("O") and x_can_beat(board, hard)
            board.remove_mark(o_row, o_col)
            if x_won:
                board.remove_mark(row, col)
                return True
        board.remove_mark(row, col)
    return False


def test_hard_never_loses_when_playing_second():
    assert x_can_beat(Board(), HardAI(random.Random(0))) is False