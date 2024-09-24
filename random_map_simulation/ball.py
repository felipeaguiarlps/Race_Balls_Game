import random

class Ball:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.path = []

    def move(self, direction):
        if direction == "up":
            self.position[0] -= 1
        elif direction == "down":
            self.position[0] += 1
        elif direction == "left":
            self.position[1] -= 1
        elif direction == "right":
            self.position[1] += 1

        self.path.append(tuple(self.position))