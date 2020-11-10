#!/usr/bin/env python3

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from logic.parser import *

class Game:
    def __init__(self):
        self.map = Map()

def main():
    game = Game()
    print("La position de start", game.map.Goal.print_pos())

main()