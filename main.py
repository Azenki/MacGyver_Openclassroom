#!/usr/bin/env python3

import random
from logic.map import Map
from graphic.gameboard import Gameboard, pygame

class Game:
    def __init__(self):
        self.map = Map()
        self.gameboard = Gameboard()
        
def main():
    game = Game()
    game.gameboard.gameloop(game.map)

main()
