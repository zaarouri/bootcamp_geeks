import random

# Constants
ROWS = 5
COLS = 5
CHIP_SYMBOL = "💎"
MISS_SYMBOL = "❌"
EMPTY_SYMBOL = "⬜"
MAX_ATTEMPTS = 10
CHIP_COUNT = 3

def create_matrix(rows, cols, fill=EMPTY_SYMBOL):
    return [[fill for _ in range(cols)] for _ in range(rows)]

def place_chips(rows, cols, chip_count):
    positions = set()
    while len(positions) < chip_count:
        pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        positions.add(pos)
    return positions

def print_matrix(matrix):
    print("   " + " ".join(str(i) for i in range(COLS)))
    for i, row in enumerate(matrix):
        print(f"{i}  " + " ".join(row))

def play_game():
    board = create_matrix(ROWS, COLS)
    chips = place_chips(ROWS, COLS, CHIP_COUNT)
    found_chips = set()
    attempts = 0
    guessed_positions = set()

    print("\nWelcome to the Chip Finder Game!")
    print(f"You have {MAX_ATTEMPTS} attempts to find {CHIP_COUNT} hidden chips.\n")

    while attempts < MAX_ATTEMPTS and len(found_chips) < CHIP_COUNT:
        print_matrix(board)
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
        except ValueError:
            print("Please enter valid integers.\n")
            continue

        if not (0 <= row < ROWS and 0 <= col < COLS):
            print("Out of bounds. Try again.\n")
            continue

        if (row, col) in guessed_positions:
            print("You already guessed that cell!\n")
            continue

        guessed_positions.add((row, col))
        attempts += 1

        if (row, col) in chips:
            board[row][col] = CHIP_SYMBOL
            found_chips.add((row, col))
            print("🎉 You found a chip!\n")
        else:
            board[row][col] = MISS_SYMBOL
            print("❌ Miss!\n")

from rich.console import Console
from rich.table import Table

console = Console()

def print_matrix(matrix):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(" ", justify="right")
    for col in range(COLS):
        table.add_column(str(col), justify="center")

    for i, row in enumerate(matrix):
        display_row = [str(i)] + row
        table.add_row(*display_row)

    console.print(table)

# Run the game
if __name__ == "__main__":
    play_game()
    