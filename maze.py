import numpy as np

class Maze:
    def __init__(self, grid, start, goal):
        # Matriz de celdas (0 = libre, 1 = obstáculo)
        self.grid = grid  
        self.start = start
        self.goal = goal
        self.venom_map = np.zeros_like(grid, dtype=float)  