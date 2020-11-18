from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *
from graphic.menu import Menu
from graphic.map import Map

class Gameboard:
    def __init__(self, map):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.jeu = Map(self.window, map.map)
