class TicTacToe:
    def __init__(self):
        self.board = [''] * 9
        self.current_player = "X"

    def print_board(self):
        print(f"[{self.board[0]}]-[{self.board[1]}]-[{self.board[2]}]")
        print(f"[{self.board[3]}]-[{self.board[4]}]-[{self.board[5]}]")
        print(f"[{self.board[6]}]-[{self.board[7]}]-[{self.board[8]}]\n")

    def check_diagonal(self):
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def check_horizontal(self):
        for i in [0, 3, 6]:
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
        return False

    def check_vertical(self):
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        return False

    def check_board(self):
        return self.check_diagonal() or self.check_horizontal() or self.check_vertical()

    def manage_turn(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def update_board(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            return True
        else:
            print("This position is already taken.\n")
            return False

    def input_position(self):
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (0-8): "))
                if position < 0 or position > 8:
                    print("Invalid position. Try again.")
                elif self.update_board(position):
                    break
            except ValueError:
                print("Please enter a number between 0 and 8.")

    def is_board_full(self):
        return all(cell != "" for cell in self.board)

    def start_game(self):
        while True:
            self.print_board()
            self.input_position()

            if self.check_board():
                self.print_board()
                print(f" Player {self.current_player} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            self.manage_turn()


# Start the game
game = TicTacToe()
game.start_game()