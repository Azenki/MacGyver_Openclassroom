import pygame
import graphic.constant
from graphic.asset import Asset


class Main_menu:
    def __init__(self):
        self.sprite = Asset(graphic.constant.MAIN_MENU_IMG, None)

    def event(self, parent, keys):
        if keys[pygame.K_RETURN]:
            parent.status = graphic.constant.STATUS_DICT["Play"]
        if keys[pygame.K_ESCAPE]:
            parent.done = True

    def draw(self, window):
        window.blit(self.sprite.image, self.sprite.rect)
