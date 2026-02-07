import unittest

import tictactoe as ttt


class TestTicTacToe(unittest.TestCase):
    def test_winner_rows(self):
        board = ["X", "X", "X", " ", "O", " ", "O", " ", " "]
        self.assertEqual(ttt.winner(board), "X")

    def test_winner_cols(self):
        board = ["O", "X", " ", "O", "X", " ", "O", " ", "X"]
        self.assertEqual(ttt.winner(board), "O")

    def test_winner_diag(self):
        board = ["X", "O", "O", " ", "X", " ", " ", " ", "X"]
        self.assertEqual(ttt.winner(board), "X")

    def test_no_winner(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertIsNone(ttt.winner(board))

    def test_is_draw_true(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(ttt.is_draw(board))

    def test_is_draw_false(self):
        board = ["X", "O", "X", " ", "O", "O", "O", "X", "X"]
        self.assertFalse(ttt.is_draw(board))

    def test_parse_move(self):
        self.assertEqual(ttt.parse_move("1"), 0)
        self.assertEqual(ttt.parse_move("9"), 8)
        self.assertIsNone(ttt.parse_move("0"))
        self.assertIsNone(ttt.parse_move("10"))
        self.assertIsNone(ttt.parse_move("a"))


if __name__ == "__main__":
    unittest.main()
