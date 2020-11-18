from logic.position import Position

class Map:
    MAP_SIZE = 16
    def __init__(self):
        element = {"Start" : 'S', "Goal" : "G"}
        self.source = list(open("map/map.txt").read())
        print(type(self.source))
        for i, letter in enumerate(self.source):
            for attr_name, attr_value in element.items():
                if letter == attr_value:
                    setattr(self, attr_name, Position(i % self.MAP_SIZE, i // self.MAP_SIZE))
