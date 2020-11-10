import curses

class Window:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.status = True

    def end(self):
        curses.endwin()