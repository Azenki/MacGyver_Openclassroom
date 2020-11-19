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
    def __init__(self, map):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.jeu = Map(self.window, map.map)
