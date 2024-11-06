import unittest
import numpy as np
from maze import Maze  

class TestMaze(unittest.TestCase):

    def setUp(self):
        # rejilla de ejemplo (0 = libre, 1 = obstáculo)
        grid = np.array([[0, 0, 1],
                         [1, 0, 0],
                         [0, 1, 0]])
        start = (0, 0)  # inicio
        goal = (2, 2)   # fin
        self.maze = Maze(grid, start, goal)

    def test_is_valid_move(self):
        self.assertTrue(self.maze.is_valid_move((0, 0)))  #  posición válida
        self.assertFalse(self.maze.is_valid_move((0, 2)))  # posición con obstáculo
        self.assertFalse(self.maze.is_valid_move((3, 0)))  # Fuera de  límites

    def test_add_venom(self):
        position = (1, 1)  
        self.maze.add_venom(position, 5)  
        self.assertEqual(self.maze.get_venom(position), 5)  

    def test_get_venom(self):
        position = (1, 1)
        self.maze.add_venom(position, 3)
        self.assertEqual(self.maze.get_venom(position), 3)

if __name__ == "__main__":
    unittest.main()