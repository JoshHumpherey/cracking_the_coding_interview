# Cracking the Coding Interview: 17.22
# Written by Josh Humphrey
import numpy as np

class Board():

    def __init__(self, number_of_moves):
        self.size = int(number_of_moves*2)
        self.grid = np.zeros((self.size, self.size))
        for r in range(self.size):
            for c in range(self.size):
                if r % 2 == 0:
                    if c % 2 == 0:
                        self.grid[r][c] = 1
                    else:
                        self.grid[r][c] = 0
                else:
                    if c % 2 == 0:
                        self.grid[r][c] = 0
                    else:
                        self.grid[r][c] = 1
    def make_move(self, r, c):
        if self.grid[r][c] == 1:
            self.grid[r][c] = 0
            np.rot90(self.grid, 2)
        else:
            self.grid[r][c] = 1
            np.rot90(self.grid, 1)

    def move_ant(self, number_of_times):
        index = 1
        r = self.size // 2
        c = self.size // 2
        while index <= number_of_times:
            self.make_move(r, c)
            r += 1
            index += 1
        self.grid[r][c] = 2
        print(self.grid)

my_grid = Board(5)
my_grid.move_ant(4)
