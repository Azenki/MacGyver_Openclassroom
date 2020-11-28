import random
from logic.position import Position
from logic.items import Item
from logic.player import Player


class Map:
    MAP_SIZE = 15
    EXCEPTIONS = ['P', 'G', 'O']

    def __init__(self):
        self.exception_pos = []
        self.list_of_item = []
        self.map = list(open("map/map.txt").read())
        while self.map.count('\n') > 0:
            self.map.remove('\n')
        for i, letter in enumerate(self.map):
            if letter == 'P':
                self.player = Player(i)
            elif letter == 'G':
                self.guardian = Position(i)
        for i in range(0, 4):
            size = len(self.exception_pos)
            while size == len(self.exception_pos):
                tmp = random.randint(0, 224)
                if self.map[tmp] not in self.EXCEPTIONS and tmp not in self.exception_pos:
                    self.exception_pos.append(tmp)
                    item = Item(tmp)
                    self.list_of_item.append(item)
