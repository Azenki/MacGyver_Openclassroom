import curses

class Window:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.status = True

    def end(self):
        curses.endwin()
    
    def move_bottom(self, pos, source):
        source[pos] = '*'
        source[pos + 16] = 'S'
    
    def move_top(self, pos, source):
        source[pos] = '*'
        source[pos - 16] = 'S'

    def move_right(self, pos, source):
        source[pos] = '*'
        source[pos + 1] = 'S'

    def move_left(self, pos, source):
        source[pos] = '*'
        source[pos - 1] = 'S'
    
    def move(self, pos, source, key):
        commands = {"End" : 10, "Right" : 67, "Up" : 65, "Down" : 66, "Left" : 68}
        index = pos.x + pos.y * 16
        if key == commands["End"]:
            self.status = False
        elif key == commands["Right"] and pos.x < 14 and source[index + 1] != '0':
            source = self.move_right(index, source)
            pos.x += 1
        elif key == commands["Left"] and pos.x > 0 and source[index - 1] != '0':
            source = self.move_left(index, source)
            pos.x -= 1
        elif key == commands["Up"] and pos.y > 0 and source[index - 16] != '0':
            source = self.move_top(index, source)
            pos.y -= 1
        elif key == commands["Down"] and pos.y < 14 and source[index + 16] != '0':
            source = self.move_bottom(index, source)
            pos.y += 1