from logic.position import Position


class Player:
    def __init__(self, pos):
        self.pos = Position(pos)

    def move_left(self, map):
        if self.pos.pos % 15 != 0 and map[self.pos.pos - 1] != 'O':
            self.pos.pos -= 1

    def move_right(self, map):
        if self.pos.pos % 15 != 14 and map[self.pos.pos + 1] != "O":
            self.pos.pos += 1

    def move_up(self, map):
        if self.pos.pos // 15 != 0 and map[self.pos.pos - 15] != 'O':
            self.pos.pos -= 15

    def move_down(self, map):
        if self.pos.pos // 15 != 14 and map[self.pos.pos + 15] != 'O':
            self.pos.pos += 15

    def get_item(self, map):
        for item in map.list_of_item:
            if self.pos.pos == item.pos.pos:
                item.status = 1
