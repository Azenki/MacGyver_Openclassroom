#!/usr/bin/env python3

import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from logic.parser import Map
from logic.items import Items
from graphic.curses import Window

class Game:
    EXCEPTION = ['0', 'S', 'G', '\n']
    ITEMS_NAME = ["Syringe", "Tube"]
    def __init__(self):
        self.map = Map()
        self.list_items = []
        exceptions_pos = []
        i = 0
        while i != 2:
            pos = random.randint(0, 225)
            if self.map.source[pos] not in self.EXCEPTION and pos not in exceptions_pos:
                self.map.source[pos] = 'I'
                self.list_items.append(Items(self.ITEMS_NAME[i], pos))
                exceptions_pos.append(pos)
                i += 1
        self.screen = Window()

def main():
    game = Game()
    #print("La position de la seringue", game.item.Syringe.print_pos())
    while game.screen.status == True:
        game.screen.screen.addstr(''.join(game.map.source))
        key = game.screen.screen.getch()
        game.screen.move(game.map.Start, game.map.source, key)
        game.screen.screen.clear()
    game.screen.end()

main()