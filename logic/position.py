class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ID = x + y * 15
    def print_pos(self):
        return (self.x, self.y, self.ID)