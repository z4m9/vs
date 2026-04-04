# Logical Noughts & Crosses
# Created by Samuel Marriott on 3/04/2026

# Facts
EMPTY_CELL = ' '
board = [[EMPTY_CELL] * 3 for _ in range(3)]
current_player = 'X'

# Rules
def row_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False

def col_win(player):
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    return False

def diag_win(player):
    return (board[0][0] == board[1][1] == board[2][2] == player) or \
           (board[0][2] == board[1][1] == board[2][0] == player)

def win(player):
    return row_win(player) or col_win(player) or diag_win(player)

def print_board():
    for row in board:
        print(' | '.join(row))
        print('---------')

# Main game loop
while True:
    print_board()
    print("Player", current_player, "turn:")
    row = int(input("Enter row number (1-3): ")) - 1
    col = int(input("Enter column number (1-3): ")) - 1

    if board[row][col] == EMPTY_CELL:
        board[row][col] = current_player

        if win(current_player):
            print_board()
            print("Player", current_player, "wins!")
            break

        elif all(cell != EMPTY_CELL for row in board for cell in row):
            print_board()
            print("It's a draw!")
            break

        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
    else:
        print("That cell is already filled. Try again.")

# Questions

# Q1. Identify and explain ONE fact.
# A. EMPTY_CELL = ' ' - A text string that contains an empty space.

# Q2. Identify and explain ONE rule
# A. def win(player) - The "win" is a function (usually) that returns a boolean.
#       The "player" is a parameter that supports the function.