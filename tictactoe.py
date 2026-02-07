#!/usr/bin/env python3
"""Simple CLI Tic-Tac-Toe with user input."""

from __future__ import annotations

from typing import List, Optional, Tuple


Player = str


def print_board(board: List[str]) -> None:
    def cell(i: int) -> str:
        return board[i] if board[i] != " " else str(i + 1)

    rows = [
        f" {cell(0)} | {cell(1)} | {cell(2)} ",
        f" {cell(3)} | {cell(4)} | {cell(5)} ",
        f" {cell(6)} | {cell(7)} | {cell(8)} ",
    ]
    sep = "---+---+---"
    print(rows[0])
    print(sep)
    print(rows[1])
    print(sep)
    print(rows[2])


def winner(board: List[str]) -> Optional[Player]:
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    return all(cell != " " for cell in board)


def parse_move(raw: str) -> Optional[int]:
    raw = raw.strip()
    if not raw.isdigit():
        return None
    idx = int(raw) - 1
    if idx < 0 or idx > 8:
        return None
    return idx


def prompt_move(board: List[str], player: Player) -> int:
    while True:
        raw = input(f"Player {player}, choose a square (1-9): ")
        idx = parse_move(raw)
        if idx is None:
            print("Invalid input. Enter a number 1-9.")
            continue
        if board[idx] != " ":
            print("That square is taken. Choose another.")
            continue
        return idx


def play_game() -> Tuple[Optional[Player], List[str]]:
    board = [" "] * 9
    current: Player = "X"

    while True:
        print_board(board)
        move = prompt_move(board, current)
        board[move] = current

        win = winner(board)
        if win:
            print_board(board)
            return win, board
        if is_draw(board):
            print_board(board)
            return None, board

        current = "O" if current == "X" else "X"


def main() -> int:
    print("Welcome to Tic-Tac-Toe!")
    win, _ = play_game()
    if win:
        print(f"Player {win} wins!")
    else:
        print("It's a draw!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
