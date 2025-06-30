class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = "X"

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}      1 | 2 | 3")
        print("---+---+---    ---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}      4 | 5 | 6")
        print("---+---+---    ---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}      7 | 8 | 9")
        print("\n")

    def input_position(self):
        while True:
            try:
                pos = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1
                if pos < 0 or pos > 8:
                    print("Invalid position. Try again.")
                elif self.board[pos] != ' ':
                    print("Position already taken. Try again.")
                else:
                    self.board[pos] = self.current_player
                    break
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def check_win(self):
        b = self.board
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        for line in wins:
            if b[line[0]] == b[line[1]] == b[line[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        while True:
            self.display_board()
            self.input_position()
            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_board_full():
                self.display_board()
                print("It's a tie!")
                break
            self.switch_player()


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
