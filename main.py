#!/usr/bin/env python3

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from logic.parser import *
from logic.items import *

class Game:
    def __init__(self):
        self.map = Map()
        self.item = Items(self.map.source)

def main():
    game = Game()
    print("La position de la seringue", game.item.Syringe.print_pos())

main()