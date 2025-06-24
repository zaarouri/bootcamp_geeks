import time
import os
import copy

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __str__(self):
        return "⬜" if self.alive else "⬛"


class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

        if initial_state:
            for r, c in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c].alive = True

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print("".join(str(cell) for cell in row))
        print()

    def count_alive_neighbors(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c].alive:
                    count += 1
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)

        for r in range(self.rows):
            for c in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(r, c)
                if self.grid[r][c].alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[r][c].alive = False
                else:
                    if alive_neighbors == 3:
                        new_grid[r][c].alive = True

        self.grid = new_grid

    def is_extinct(self):
        return all(not cell.alive for row in self.grid for cell in row)

    def run(self, generations=10, delay=0.5):
        for gen in range(generations):
            print(f"Generation {gen + 1}")
            self.display()
            if self.is_extinct():
                print("All cells are dead. Game over.")
                break
            self.next_generation()
            time.sleep(delay)


# Initial state (Glider)
initial_cells = [
    (1, 2),
    (2, 3),
    (3, 1), (3, 2), (3, 3)
]

game = GameOfLife(rows=10, cols=10, initial_state=initial_cells)
game.run(generations=20, delay=0.3)
