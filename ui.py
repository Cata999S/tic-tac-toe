"""
The game's user interface
    - The only place where we have print and input statements!
"""

from game import *

"""
How the UI should work:
    1. Show the (initially empty) game board
        -> we do this by calling to_str() from the board module
    2. Read the human player's move
        -> catch any ValueError and print out its message
        -> repeat reading the move until the move is valid :)
    3. Calculate and make the computer's move
    4. Show the board again
    5. Go back to step 2.
        -> After each move (human or computer) check for the win
        -> The player who moved last won
        -> If the board is full AND the game was not won, it's a draw.
    6. When the game ends, display the final state of the board and print a corresponding
    message
"""

def print_board(board):
    print(to_str(board))
def main():
    board = create_board()
    print("Welcome to my tic tac toe!!!")
    i = 0
    while not is_full_board(board) and not is_board_won(board):
        print_board(board)
        try:
            c1,c2 = int(input("Please enter the first position (0-2): ")), int(input("Please enter the second position (0-2): "))
            move_human(board, c1, c2)
            print_board(board)
            print("The computer makes a move...")
            move_computer(board)
        except ValueError as e:
            print(e)
    if i % 2 == 0 and is_board_won(board):
        print("You won!")
    elif i % 2 == 1 and is_board_won(board):
        print("You lost!")
    else:
        print("Draw!")




