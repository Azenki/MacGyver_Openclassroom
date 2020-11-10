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
        key = game.screen.screen.getch()
        game.screen.screen.refresh()
        if key == 10:
            game.screen.status = False
        game.screen.screen.clear()
    game.screen.end()

main()