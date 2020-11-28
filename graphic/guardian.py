import pygame
import graphic.constant as const
from graphic.asset import Asset


class Guardian:
    def __init__(self):
        self.sprite = Asset(const.GUARDIAN_IMG, pygame.Rect(0, 0, 32, 32))

    def draw(self, window, pos):
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)
