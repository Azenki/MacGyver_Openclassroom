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