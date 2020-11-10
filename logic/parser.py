class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_pos(self):
        return (self.x, self.y)

class Map:
    def __init__(self):
        element = {"Syringe" : '1', "Tube" : '2', "Start" : 'S', "Goal" : "G", "Map_size" : 16}
        self.source = open("map/map.txt").read()
        for i, letter in enumerate(self.source):
            for attr_name, attr_value in element.items():
                if letter == attr_value:
                    setattr(self, attr_name, Position(i % element["Map_size"],i // element["Map_size"]))
