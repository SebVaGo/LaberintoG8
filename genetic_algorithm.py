import random
from individual import Individual

class GeneticAlgorithm:
    def __init__(self, maze, population_size=50,  mutation_rate=0.1,elitism=True,stagnation_limit=10, max_path_length=50):
        self.maze = maze
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_path_length = max_path_length
        self.elitism = elitism
        self.stagnation_limit = stagnation_limit
        self.population = self._initialize_population()
    
    def _mutate(self, individual):
        """Aplica mutación en un individuo, asegurando que solo realice movimientos en direcciones cardinales y válidos."""
        last_position = individual.get_last_position()
        venom_level = self.maze.get_venom(last_position)

        # Incrementa la probabilidad de exploración si el veneno es alto
        exploration_probability = 0.7 if venom_level > 2 else 0.3
        if random.random() < exploration_probability or individual.venom_count > 3:
            visited_positions = set(individual.path)

            # Exploración aleatoria solo en direcciones cardinales y válidas
            all_moves = [
                (last_position[0] + 1, last_position[1]),  # Abajo
                (last_position[0] - 1, last_position[1]),  # Arriba
                (last_position[0], last_position[1] + 1),  # Derecha
                (last_position[0], last_position[1] - 1)   # Izquierda
            ]
            random.shuffle(all_moves)
            valid_moves = [move for move in all_moves if move not in visited_positions and self.maze.is_valid_move(move)]
            new_step = valid_moves[0] if valid_moves else None

            if new_step:
                individual.add_step(new_step, self.maze)
                individual.calculate_fitness(self.maze)
            else:
                # Retroceso en caso de callejón sin salida
                individual.backtrack()
        else:
            # Retroceso automático si hay estancamiento
            individual.backtrack()

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
