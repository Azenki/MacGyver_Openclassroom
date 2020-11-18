from logic.position import Position
import random

class Items:
    MAP_SIZE = 16
    def __init__(self, source):
        i = 0
        print(type(source))
        while i != 2:
            pos = random.randint(0, 225)
            if source[pos] != 0:
                source[pos] = 'L'
                i += 1