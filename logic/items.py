from logic.position import Position


class Item:
    def __init__(self, pos):
        self.status = 0
        self.pos = Position(pos)
