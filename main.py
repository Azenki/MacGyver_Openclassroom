#!/usr/bin/env python3

import random
from logic.map import Map
from graphic.gameboard import Gameboard, pygame

class Game:
    def __init__(self):
        self.map = Map()
        self.gameboard = Gameboard(self.map)

def gameloop():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()
        
def main():
    game = Game()
    game.map.print_map()
    gameloop()

main()
