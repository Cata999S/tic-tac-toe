"""
Functions that have to do with the game board
"""
from texttable import Texttable


def create_board() -> list:
    """
    Create the (initially empty) game board. We represent the board as a 3x3 matrix (one Python list
    that has 3 sub-lists of length 3 each).

    How to represent things on the board:
        -1 -> empty square
         0 -> 'O'
         1 -> 'X'
    """
    return [[' ' for _ in range(3)] for _ in range(3)]

def get_value_on_board(board: list, row: int, col: int) -> int:
    """
    Return the value on the board at (row, col) coordinates
    :param board:
    :param row:
    :param col:
    :return: -1 if its an empty square, 0 if it's an 'O' and 1 if it's an 'X'
    """
    return board[row][col]


def move_board(board: list, symbol: str, row: int, col: int):
    """
    Record a move on the board
    :param board: the game board
    :param symbol: One of 'X' (human player), or 'O' (computer player)
    :param row: The row, one of 0, 1 or 2
    :param col: The column, one of 0, 1 or 2
    :return: None
    :raises ValueError if:
        - move would be outside the board
        - symbol is not one of 'X' or 'O'
        - the (row, col) position already has a symbol on it
    """
    value = get_value_on_board(board, row, col)
    if row > 2 or row < 0:
        raise ValueError("The move would be outside of the board")
    if col > 2 or col < 0:
        raise ValueError("The move would be outside of the board")
    if value == 'X' or value == 'O':
        raise ValueError("The position already has a symbol on it")
    elif value == ' ':
        board[row][col] = symbol
    else:
        raise ValueError("Symbol is invalid")


def is_full_board(board: list) -> bool:
    """
    Check whether the game board is full
    :param board: the board
    :return: True if the board is full, False otherwise
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                return False
    return True


def is_board_won(board: list) -> bool:
    """
    Check whether the game board is won by either player
    :param board: the board
    :return: True if the board is won, False otherwise
    """
    if ( board[0][0] == board[1][1] == board[2][2] == 'O' ) or ( board[0][0] == board[1][1] == board[2][2] == 'X' ):
        return True
    if ( board[2][0] == board[1][1] == board[0][2] == 'O' ) or ( board[2][0] == board[1][1] == board[0][2] == 'X' ):
        return True
    for j in range(len(board)):
        if ( board[0][j] == board[1][j] == board[2][j] == 'O' ) or ( board[0][j] == board[1][j] == board[2][j] == 'X' ):
            return True
    for i in range(len(board)):
        if ( board[i][0] == board[i][1] == board[i][2] == 'O' ) or ( board[i][0] == board[i][1] == board[i][2] == 'X' ):
            return True
    return False


def to_str(board: list) -> str:
    """
    Return the string representation of the board. Use the texttable component to pretty print it
    :param board: The game board
    """
    t = Texttable()
    for row in board:
        t.add_row(row)
    return t.draw()
