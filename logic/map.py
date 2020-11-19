import random
from logic.position import Position
from logic.items import Item

class Map:
    #size plus one for the return "\n"
    MAP_SIZE = 15
    EXCEPTIONS = ['P', 'G', 'O']
    ITEMS_NAME = ["Syringe", "Tube"]
    def __init__(self):
        self.exception_pos = []
        self.map = list(open("map/map.txt").read())
        while self.map.count('\n') > 0:
            self.map.remove('\n')
        for i, letter in enumerate(self.map):
            if letter == 'P':
                self.player = Position(i)
            elif letter == 'G':
                self.guardian = Position(i)
        i = 0
        while i != 2:
            tmp = random.randint(0, 224)
            if self.map[tmp] not in self.EXCEPTIONS and tmp not in self.exception_pos:
                self.map[tmp] = str(i)
                setattr(Item, self.ITEMS_NAME[i], tmp)
                i += 1