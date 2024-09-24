import random

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = self.generate_random_map()

    def generate_random_map(self):
        return [[random.choice(['.', '#', 'O']) for _ in range(self.size)] for _ in range(self.size)]

    def display(self):
        for row in self.grid:
            print(" ".join(row))