import random
from individual import Individual

class GeneticAlgorithm:
    def __init__(self, maze, population_size=50, elitism=True, max_path_length=50):
        self.maze = maze
        self.population_size = population_size
        self.max_path_length = max_path_length
        self.elitism = elitism
        self.population = self._initialize_population()

    def _initialize_population(self):
        """Inicializa la población de individuos en el laberinto."""
        population = []
        for _ in range(self.population_size):
            individual = Individual(self.maze, [self.maze.start])
            visited_positions = set(individual.path)
            for _ in range(self.max_path_length):
                last_position = individual.get_last_position()
                next_step = self._directed_move(last_position, visited_positions)
                if next_step:
                    individual.add_step(next_step, self.maze)
                    visited_positions.add(next_step)
            individual.calculate_fitness(self.maze)
            population.append(individual)
        return population

    def _selection(self):
        """Selecciona a los mejores individuos de la población según su fitness."""
        self.population.sort(key=lambda individual: individual.fitness, reverse=True)
        return self.population[:self.population_size // 2]

    def _directed_move(self, position, visited_positions):
        """Determina un movimiento dirigido hacia la meta en el laberinto."""
        x, y = position
        goal_x, goal_y = self.maze.goal
        moves = []

        # Movimientos dirigidos solo en direcciones cardinales
        if goal_x > x:
            moves.append((x + 1, y))  # Abajo
        elif goal_x < x:
            moves.append((x - 1, y))  # Arriba
        if goal_y > y:
            moves.append((x, y + 1))  # Derecha
        elif goal_y < y:
            moves.append((x, y - 1))  # Izquierda

        valid_moves = [move for move in moves if move not in visited_positions and self.maze.is_valid_move(move)]
        return valid_moves[0] if valid_moves else None
