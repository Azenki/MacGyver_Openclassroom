import pygame
import os
from os.path import dirname, abspath
from graphic.asset import Asset

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
GUARDIAN_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "Gardien.png"))

class Guardian:
    def __init__(self):
        self.sprite = Asset(GUARDIAN_IMG, pygame.Rect(0, 0, 32, 32))

    def draw(self, window, pos):
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)