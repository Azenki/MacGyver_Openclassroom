#!/usr/bin/env python3

import random
from logic.map import Map
from graphic.graphic import Graphic, pygame

class Game:
    def __init__(self):
        self.map = Map()
        self.graphic = Graphic()
        
def main():
    game = Game()
    game.graphic.gameloop(game.map)

main()
