import pygame
import os
from os.path import dirname, abspath
from graphic.asset import Asset

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
MENU_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "main_menu.png"))


class Main_menu:
    def __init__(self):
        self.sprite = Asset(MENU_IMG, MENU_IMG.get_rect())

    def draw(self, window):
        window.blit(self.sprite.image, self.sprite.rect)
