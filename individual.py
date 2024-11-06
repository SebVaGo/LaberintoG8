from maze import Maze

class Individual:
    # Inicializa un individuo con una ruta, estado de objetivo, conteo de veneno y pasos estancados
    def __init__(self, maze, path=None):
        self.path = path if path else []
        self.fitness = 0
        self.goal_reached = False
        self.goal = maze.goal
        self.venom_count = 0
        self.visited_positions = set(self.path)
        self.stagnant_steps = 0
    
    # Agrega un paso a la ruta del individuo si es un movimiento cardinal y es válido en el laberinto
    def add_step(self, step, maze):
        if self._is_cardinal_move(self.get_last_position(), step) and maze.is_valid_move(step) and not self.goal_reached:
            # Verifica que el movimiento sea cardinal y válido
            if step in self.visited_positions:
                self.venom_count += 5
                self.stagnant_steps += 5
            else:
                self.path.append(step) # Agrega el nuevo paso a la ruta
                self.visited_positions.add(step) # Registra el paso como visitado
            
            # Si se alcanza el objetivo, actualiza el estado y resetea contadores de penalización
            if step == self.goal:
                self.goal_reached = True
                self.venom_count = 0
                self.stagnant_steps = 0
            
            # Agrega veneno a la posición en el laberinto para penalizar futuros pasos allí
            maze.add_venom(step, amount=3)
    
    # Retrocede en la ruta si el individuo se estanca, eliminando el último paso
    def backtrack(self):
        if len(self.path) > 1:
            last_step = self.path.pop()
            self.visited_positions.discard(last_step)
            self.stagnant_steps += 2
        return self.path[-1] if self.path else None

    #Retorna la última posición
    def get_last_position(self):
        return self.path[-1] if self.path else None

    #Calculo del fitness con movimientos cardinales y penalización por bucle
    def calculate_fitness(self, maze):
        # Calcula la distancia al objetivo
        distance_to_goal = abs(self.path[-1][0] - maze.goal[0]) + abs(self.path[-1][1] - maze.goal[1])
        self.fitness = -distance_to_goal * 20
       
        # Penaliza los bucles (visitar posiciones repetidas)
        unique_positions = len(self.visited_positions)
        loop_penalty = (len(self.path) - unique_positions) * 30
        self.fitness -= loop_penalty + (self.stagnant_steps * 30)
       
        # Penalización acumulada de veneno en la ruta
        venom_penalty = sum(maze.get_venom(pos) for pos in self.path)
        self.fitness -= venom_penalty
        
        # Bonificación si se alcanza el objetivo
        if distance_to_goal == 0:
            self.fitness += 2000

    #verifica si el movimiento entre dos posiciones es cardinal
    def _is_cardinal_move(self, current_pos, new_pos):
        if current_pos is None:
            return True
        x1, y1 = current_pos
        x2, y2 = new_pos
        return (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)
