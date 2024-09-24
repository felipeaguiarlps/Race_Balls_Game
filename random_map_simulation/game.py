from random.map import Map
from random.ball import Ball
import random

def play_game():
    # Inicializar mapa
    size = 10
    game_map = Map(size)

    # Inicializar bolinhas
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    balls = [Ball(color, [random.randint(0, size-1), random.randint(0, size-1)]) for color in colors]

    # Simulação
    steps = 20
    for _ in range(steps):
        for ball in balls:
            direction = random.choice(["up", "down", "left", "right"])
            ball.move(direction)

    # Exibir resultados
    game_map.display()
    for ball in balls:
        print(f"{ball.color} Ball Path: {ball.path}")

if __name__ == "__main__":
    play_game()
