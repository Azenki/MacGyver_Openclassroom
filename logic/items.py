class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_pos(self):
        return (self.x, self.y)

class Items:
    def __init__(self, source):
        element = {"Syringe" : '1', "Tube" : '2', "Map_size" : 16}
        for i, letter in enumerate(source):
            for attr_name, attr_value in element.items():
                if letter == attr_value:
                    setattr(self, attr_name, Position(i % element["Map_size"],i // element["Map_size"]))