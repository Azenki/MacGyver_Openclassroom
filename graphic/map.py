import pygame
import graphic.constant as const
from graphic.asset import Asset


class Map:
    def __init__(self):
        self.wall = Asset(const.SPRITE_SHEET, pygame.Rect(96, 0, 32, 32))
        self.road = Asset(const.SPRITE_SHEET, pygame.Rect(32, 32, 32, 32))

    def draw(self, window, map):
        for i, letter in enumerate(map):
            x = i % 15 * 32
            y = i // 15 * 32
            if letter == 'O':
                self.wall.rect.x = x
                self.wall.rect.y = y
                window.blit(self.wall.image, self.wall.rect)
            else:
                self.road.rect.x = x
                self.road.rect.y = y
                window.blit(self.road.image, self.road.rect)
