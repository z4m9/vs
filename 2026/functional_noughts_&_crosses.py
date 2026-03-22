# Created by Samuel Marriott on 22/03/2026
# Functional-style Tic-Tac-Toe in Python

def print_board(board):
    """Display the current board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    """Return True if the specified player has won."""
    # Check rows
    if any(all(cell == player for cell in row) for row in board):
        return True

    # Check columns
    if any(all(board[row][col] == player for row in range(3)) for col in range(3)):
        return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Return True if there are no empty spaces left on the board."""
    return all(cell != " " for row in board for cell in row)


def get_move(player):
    """Ask the player for a move from 1 to 9."""
    move = input(f"Player {player}, enter your move (1-9): ")

    if move.isdigit():
        move = int(move)
        if 1 <= move <= 9:
            return move

    return None


def is_cell_empty(board, move):
    """Return True if the chosen board position is empty."""
    row = (move - 1) // 3
    col = (move - 1) % 3
    return board[row][col] == " "


def update_board(board, move, player):
    """
    Return a new board with the player's move added.
    This does not directly change the original board.
    """
    row = (move - 1) // 3
    col = (move - 1) % 3

    return [
        [
            player if (r, c) == (row, col) else board[r][c]
            for c in range(3)
        ]
        for r in range(3)
    ]


def game_loop(board, current_player):
    """Run the main game loop."""
    while True:
        print_board(board)

        move = None
        while move is None:
            move = get_move(current_player)

            if move is None:
                print("Invalid input. Please enter a number from 1 to 9.")
            elif not is_cell_empty(board, move):
                print("That cell is already taken. Choose another one.")
                move = None

        # Functional-style update: create a new board rather than changing the old one
        board = update_board(board, move, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_loop(board, "X")


if __name__ == "__main__":
    main()
