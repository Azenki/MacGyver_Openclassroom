class Position:
    def __init__(self, pos):
        self.pos = pos
        self.x = pos % 15
        self.y = pos // 15

    def print_pos(self):
        return (pos, x, y)
