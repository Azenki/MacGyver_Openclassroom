import pygame
import graphic.constant
from graphic.asset import Asset

class Pause_menu:
    def __init__(self):
        self.sprite = Asset(graphic.constant.PAUSE_MENU_IMG, None)

    def event(self, parent, keys):
        if keys[pygame.K_RETURN]:
            parent.status = graphic.constant.STATUS_DICT["Play"]
        elif keys[pygame.K_ESCAPE]:
            parent.status = graphic.constant.STATUS_DICT["Main_menu"]

    def draw(self, window):
        window.blit(self.sprite.image, self.sprite.rect)
