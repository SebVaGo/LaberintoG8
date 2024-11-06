import random
import time  # Para usar time.sleep
from maze import Maze
from genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt
import numpy as np

def plot_path_step_by_step(maze, path, line):
    """Visualiza el camino paso a paso, actualizando la línea roja en cada paso."""
    for i in range(1, len(path) + 1):
        x_coords, y_coords = zip(*path[:i])  # Mostrar solo hasta el paso actual
        line.set_data(y_coords, x_coords)  # Actualiza los datos de la línea
        plt.draw()
        plt.pause(0.1)  # Pausa para actualizar el gráfico
        time.sleep(0.2)  # Pausa para ver el movimiento de cada paso

# Definir un laberinto de ejemplo
grid = [
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
]
start = (0, 0)
goal = (9, 9)

maze = Maze(grid, start, goal)

# Configuración de la visualización
plt.ion()  # Activa el modo interactivo
fig, ax = plt.subplots()
ax.imshow(np.array(maze.grid), cmap="Greys", origin="upper")

# Marcar inicio y objetivo
ax.plot(maze.start[1], maze.start[0], "bo", markersize=10, label="Inicio")
ax.plot(maze.goal[1], maze.goal[0], "g*", markersize=10, label="Objetivo")

# Crear la línea para el camino y configurar la leyenda
line, = ax.plot([], [], "ro-", markersize=5, label="Camino")
plt.legend()

# Ejecutar el algoritmo genético
ga = GeneticAlgorithm(maze)
best_found = False

for generation in range(100):  # Ejecuta varias generaciones
    best_route = ga.run(generations=1)

    # Verificar si se alcanzó el objetivo
    if best_route.goal_reached:
        best_found = True
    
    # Visualizar el camino del mejor individuo paso a paso
    plot_path_step_by_step(maze, best_route.path, line)
    
    if best_found:
        break  # Detener la ejecución cuando se encuentra la mejor ruta

# Visualizar la mejor ruta final
plt.ioff()  # Desactiva el modo interactivo
plt.show()
print("Mejor ruta encontrada:", best_route.path)
