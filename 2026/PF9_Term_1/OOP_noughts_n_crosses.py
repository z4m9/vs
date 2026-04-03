# OOP Noughts & Crosses
# Created by Samuel Marriott on 3/04/2026
# Questions and answers after line 71

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)

    def make_move(self, row, col, player):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def play(self):
        while True:
            self.board.print_board()

            row = int(input(f"Player {self.current_player}, enter row (0-2): "))
            col = int(input(f"Player {self.current_player}, enter column (0-2): "))

            if self.board.make_move(row, col, self.current_player):
                if self.board.check_winner(self.current_player):
                    self.board.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.board.is_full():
                    self.board.print_board()
                    print("It's a draw!")
                    break
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()

# Analysis:
# Q1. Identify the name of one class.
# A. TicTacToeGame
# Q2. Identify two attributes used in the program. Look for variables that use self.
# A. board, current_player
# Q3. Identify one method (not a constructor) and the class it belongs to.
# A. The "print_board" method - belongs to the "Board" class.

# Challenge:
# Q1. 