from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *
from graphic.menu import Menu
from graphic.map import Map
from graphic.player import Player

WIDTH = 800
HEIGHT = 600
FPS = 5

class Gameboard:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map()
        self.player = Player()
        self.clock = pygame.time.Clock()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def draw_game(self, map):
        self.window.fill("black")
        self.map.draw(self.window, map.map)
        self.player.draw(self.window, map.player.pos)

    def draw_menu(self):
        pass

    def gameloop(self, map):
        done = False
        while not done:
            self.clock.tick(FPS)
            done = self.event_loop()
            self.player.move(map)
            self.draw_game(map)
            pygame.display.flip()
