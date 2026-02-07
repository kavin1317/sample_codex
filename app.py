#!/usr/bin/env python3
"""Streamlit UI for Tic-Tac-Toe."""

from __future__ import annotations

import streamlit as st

import tictactoe as ttt


st.set_page_config(page_title="Tic-Tac-Toe", page_icon="❌", layout="centered")


if "board" not in st.session_state:
    st.session_state.board = [" "] * 9
if "current" not in st.session_state:
    st.session_state.current = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None
if "draw" not in st.session_state:
    st.session_state.draw = False


def reset_game() -> None:
    st.session_state.board = [" "] * 9
    st.session_state.current = "X"
    st.session_state.winner = None
    st.session_state.draw = False


def make_move(idx: int) -> None:
    if st.session_state.winner or st.session_state.draw:
        return
    if st.session_state.board[idx] != " ":
        return
    st.session_state.board[idx] = st.session_state.current
    win = ttt.winner(st.session_state.board)
    if win:
        st.session_state.winner = win
        return
    if ttt.is_draw(st.session_state.board):
        st.session_state.draw = True
        return
    st.session_state.current = "O" if st.session_state.current == "X" else "X"


st.title("Tic-Tac-Toe")

status = ""
if st.session_state.winner:
    status = f"Player {st.session_state.winner} wins!"
elif st.session_state.draw:
    status = "It’s a draw!"
else:
    status = f"Player {st.session_state.current}'s turn"

st.subheader(status)

st.caption("Click a square or enter a move number (1-9).")

board = st.session_state.board

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        label = board[idx] if board[idx] != " " else str(idx + 1)
        if cols[col].button(label, key=f"cell_{idx}", use_container_width=True):
            make_move(idx)

with st.form("move_form"):
    move = st.text_input("Enter move (1-9)", value="", max_chars=2)
    submitted = st.form_submit_button("Submit move")
    if submitted:
        idx = ttt.parse_move(move) if move else None
        if idx is None:
            st.warning("Invalid input. Enter a number 1-9.")
        else:
            make_move(idx)

st.button("Reset", on_click=reset_game)
