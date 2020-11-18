from logic.position import Position
import random

class Items:
    MAP_SIZE = 16
    def __init__(self, name, pos):
        self.name = name
        self.pos = Position(pos % 15, pos // 15)
