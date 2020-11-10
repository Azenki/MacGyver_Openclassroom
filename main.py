#!/usr/bin/env python3

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from logic.parser import *
from logic.items import *
from graphic.curses import * 

class Game:
    def __init__(self):
        self.map = Map()
        self.item = Items(self.map.source)
        self.screen = Window()

def main():
    game = Game()
    #print("La position de la seringue", game.item.Syringe.print_pos())
    while game.screen.status == True:
        game.screen.screen.addstr(game.map.source)
        commands = {"End" : 10, "Right" : 67, "Up" : 65, "Down" : 66, "Left" : 68}
        key = game.screen.screen.getch()
        game.screen.screen.refresh()
        if key == commands["End"]:
            game.screen.status = False
        elif key == commands["Right"] and game.map.Start.x < 14:
            game.map.source = game.screen.move_right(game.map.Start, game.map.source)
            game.map.Start.x += 1
        elif key == commands["Left"] and game.map.Start.x > 0:
            game.map.source = game.screen.move_left(game.map.Start, game.map.source)
            game.map.Start.x -= 1
        elif key == commands["Up"] and game.map.Start.y > 0:
            game.map.source = game.screen.move_top(game.map.Start, game.map.source)
            game.map.Start.y -= 1
        elif key == commands["Down"] and game.map.Start.y < 14:
            game.map.source = game.screen.move_bottom(game.map.Start, game.map.source)
            game.map.Start.y += 1
        game.screen.screen.clear()
    game.screen.end()
65
main()