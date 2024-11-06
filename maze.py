import numpy as np

class Maze:
    def __init__(self, grid, start, goal):
        # Matriz de celdas (0 = libre, 1 = obstáculo)
        self.grid = grid  
        self.start = start
        self.goal = goal
        self.venom_map = np.zeros_like(grid, dtype=float)  

    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] == 0
        return False
