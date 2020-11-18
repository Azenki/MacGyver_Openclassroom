#!/usr/bin/env python3

import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from logic.map import Map

class Game:
    def __init__(self):
        self.map = Map()

def main():
    game = Game()
    game.map.print_map()

main()
