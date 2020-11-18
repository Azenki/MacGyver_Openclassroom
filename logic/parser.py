from logic.position import Position

class Map:
    def __init__(self):
        element = {"Start" : 'S', "Goal" : "G", "Map_size" : 16}
        self.source = open("map/map.txt").read()
        for i, letter in enumerate(self.source):
            for attr_name, attr_value in element.items():
                if letter == attr_value:
                    setattr(self, attr_name, Position(i % element["Map_size"],i // element["Map_size"]))
