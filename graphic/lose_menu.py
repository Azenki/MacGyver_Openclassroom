import pygame
import graphic.constant
from graphic.asset import Asset


class Lose_menu:
    def __init__(self):
        self.sprite = Asset(graphic.constant.LOSE_MENU_IMG, None)

    def draw(self, window):
        window.blit(self.sprite.image, self.sprite.rect)

    def loop(self, parent, window):
        self.draw(window)
