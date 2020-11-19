from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *
from graphic.menu import Menu
from graphic.map import Map

WIDTH = 800
HEIGHT = 600
FPS = 30

class Gameboard:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map()

    def gameloop(self, map):
        done = False
        while not done:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                   done = True
            self.window.fill("black")
            self.map.draw(self.window, map.map)
            pygame.display.flip()
