from maze import Maze

class Individual:
   def __init__(self, maze, path=None): #inicializar las variables 
   self.path = path if path else []
   self.fitness = 0
   self.goal_reached = False
   self.goal = maze.goal
   self.venom_count = 0 
   self.visited_positions = set(self.path)
   self.stagnant_steps = 0