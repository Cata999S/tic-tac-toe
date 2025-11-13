"""
This is where we add the logic to make moves on the board
"""
import random
from board import *

def move_human(board: list, row: int, col: int):
    """
    Record the human player's move on the board
    :param board:
    :param row:
    :param col:
    """
    move_board(board, "X", row, col)


def move_computer(board: list) -> tuple:
    """
    Calculate the computer's move and make it. The computer makes random, but valid moves on
    the board.
    :param board: the board

    There should be no exceptions here, because the computer should validate the validity
    of its moves.
    """
    if is_full_board(board):
        return (board,None, None)
    while True:
        r, c = random.randint(0, 2), random.randint(0, 2)
        if get_value_on_board(board, r, c) == ' ':
            move_board(board, "O", r, c)
            return (board, r, c)

