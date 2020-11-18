from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *


class Gameboard:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((400, 300))
        """done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()
"""
