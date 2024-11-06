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
   
   #lógica para agregar un paso a la ruta del individuo
   def add_step(self, step, maze):
      if self._is_cardinal_move(self.get_last_position(), step) and maze.is_valid_move(step) and not self.goal_reached:
         if step in self.visited_positions:
               self.venom_count += 5
               self.stagnant_steps += 5
         else:
               self.path.append(step)
               self.visited_positions.add(step)
               
         if step == self.goal:
               self.goal_reached = True
               self.venom_count = 0
               self.stagnant_steps = 0
               
         maze.add_venom(step, amount=3)  
         
   #retroceder en caso se estanque    
   def backtrack(self):
      if len(self.path) > 1:
         last_step = self.path.pop()
         self.visited_positions.discard(last_step)
         self.stagnant_steps += 2  # Penaliza el retroceso
      return self.path[-1] if self.path else None
   