import pytest

import tictactoe as ttt


@pytest.mark.parametrize(
    "board, expected",
    [
        (["X", "X", "X", " ", "O", " ", "O", " ", " "], "X"),
        (["O", "X", " ", "O", "X", " ", "O", " ", "X"], "O"),
        (["X", "O", "O", " ", "X", " ", " ", " ", "X"], "X"),
    ],
)
def test_winner(board, expected):
    assert ttt.winner(board) == expected


def test_no_winner():
    board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert ttt.winner(board) is None


def test_is_draw():
    full_board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    not_full = ["X", "O", "X", " ", "O", "O", "O", "X", "X"]
    assert ttt.is_draw(full_board) is True
    assert ttt.is_draw(not_full) is False


@pytest.mark.parametrize(
    "raw, expected",
    [("1", 0), ("9", 8), ("0", None), ("10", None), ("a", None)],
)
def test_parse_move(raw, expected):
    assert ttt.parse_move(raw) == expected
