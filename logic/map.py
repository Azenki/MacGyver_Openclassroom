import random
from logic.position import Position
from logic.items import Item

class Map:
    #size plus one for the return "\n"
    MAP_SIZE = 16
    EXCEPTIONS = ['P', 'G', 'O', '\\n']
    ITEMS_NAME = ["Syringe", "Tube"]
    def __init__(self):
        self.list_item = []
        self.exception_pos = []
        self.map = list(open("map/map.txt").read())
        for i, letter in enumerate(self.map):
            if letter == 'P':
                self.player = Position(i)
            elif letter == 'G':
                self.goal = Position(i)
        i = 0
        while i != 2:
            tmp = random.randint(0, 256)
            if tmp not in self.EXCEPTIONS and tmp not in self.exception_pos:
                self.map[tmp] = str(i)
                self.list_item.append(setattr(Item, self.ITEMS_NAME[i], tmp))
                i += 1

    def print_map(self):
        print(''.join(self.map))
