import pygame
import os
from os.path import dirname, abspath
from graphic.asset import Asset

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
SYRINGE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "seringue.png"))
TUBE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "tube_plastique.png"))

class Items:
    def __init__(self):
        self.SYRINGE_RESIZE = pygame.transform.scale(SYRINGE_IMG, (32, 32))
        self.TUBE_RESIZE = pygame.transform.scale(TUBE_IMG, (32, 32))
        self.SYRINGE_RESIZE.convert_alpha()
        self.syringe = Asset(self.SYRINGE_RESIZE, self.SYRINGE_RESIZE.get_rect())
        self.tube = Asset(self.TUBE_RESIZE, self.TUBE_RESIZE.get_rect())
    
    def draw(self,window, map):
        for i, letter in enumerate(map):
            x = i % 15 * 32
            y = i // 15 * 32
            if letter == '0':
                self.syringe.rect.x = x
                self.syringe.rect.y = y
                window.blit(self.syringe.image, self.syringe.rect)
            elif letter == '1':
                self.tube.rect.x = x
                self.tube.rect.y = y
                window.blit(self.tube.image, self.tube.rect)