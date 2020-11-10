import curses

class Window:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.status = True

    def end(self):
        curses.endwin()
    
    def move_bottom(self, pos, source):
        index = pos.x + pos.y * 16
        tmp = list(source)
        tmp[index] = '*'
        tmp[index + 16] = 'S'
        new = ''.join(tmp)
        return (new)
    
    def move_top(self, pos, source):
        index = pos.x + pos.y * 16
        tmp = list(source)
        tmp[index] = '*'
        tmp[index - 16] = 'S'
        new = ''.join(tmp)
        return (new)

    def move_right(self, pos, source):
        index = pos.x + pos.y * 16
        tmp = list(source)
        tmp[index] = '*'
        tmp[index + 1] = 'S'
        new = ''.join(tmp)
        return (new)

    def move_left(self, pos, source):
        index = pos.x + pos.y * 16
        tmp = list(source)
        tmp[index] = '*'
        tmp[index - 1] = 'S'
        new = ''.join(tmp)
        return (new)
    
    def move(self, pos, source, game, key):
        commands = {"End" : 10, "Right" : 67, "Up" : 65, "Down" : 66, "Left" : 68}
        if key == commands["End"]:
            self.status = False
        elif key == commands["Right"] and pos.x < 14:
            game.map.source = self.move_right(pos, game.map.source)
            pos.x += 1
        elif key == commands["Left"] and pos.x > 0:
            game.map.source = self.move_left(pos, game.map.source)
            pos.x -= 1
        elif key == commands["Up"] and pos.y > 0:
            game.map.source = self.move_top(pos, game.map.source)
            pos.y -= 1
        elif key == commands["Down"] and pos.y < 14:
            game.map.source = self.move_bottom(pos, game.map.source)
            pos.y += 1