import curses

class Window:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.status = True

    def end(self):
        curses.endwin()
    
    def move_bottom(self, pos, source, tab):
        tab[pos] = '*'
        tab[pos + 16] = 'S'
        new = ''.join(tab)
        return (new)
    
    def move_top(self, pos, source, tab):
        tab[pos] = '*'
        tab[pos - 16] = 'S'
        new = ''.join(tab)
        return (new)

    def move_right(self, pos, source, tab):
        tab[pos] = '*'
        tab[pos + 1] = 'S'
        new = ''.join(tab)
        return (new)

    def move_left(self, pos, source, tab):
        tab[pos] = '*'
        tab[pos - 1] = 'S'
        new = ''.join(tab)
        return (new)
    
    def move(self, pos, source, game, key):
        commands = {"End" : 10, "Right" : 67, "Up" : 65, "Down" : 66, "Left" : 68}
        tab = list(source)
        index = pos.x + pos.y * 16
        if key == commands["End"]:
            self.status = False
        elif key == commands["Right"] and pos.x < 14 and tab[index + 1] != '0':
            game.map.source = self.move_right(index, game.map.source, tab)
            pos.x += 1
        elif key == commands["Left"] and pos.x > 0 and tab[index - 1] != '0':
            game.map.source = self.move_left(index, game.map.source, tab)
            pos.x -= 1
        elif key == commands["Up"] and pos.y > 0 and tab[index - 16] != '0':
            game.map.source = self.move_top(index, game.map.source, tab)
            pos.y -= 1
        elif key == commands["Down"] and pos.y < 14 and tab[index + 16] != '0':
            game.map.source = self.move_bottom(index, game.map.source, tab)
            pos.y += 1