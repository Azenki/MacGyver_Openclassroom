import pygame
import graphic.constant as const
from graphic.asset import Asset

""" Module of Map
"""


class Map:
    """ Class of map init and draw the map
    """
    def __init__(self):
        """__init__ the map sprite
        """
        self.wall = Asset(const.SPRITE_SHEET, pygame.Rect(96, 0, 32, 32))
        self.road = Asset(const.SPRITE_SHEET, pygame.Rect(32, 32, 32, 32))

    def draw(self, window, map):
        """draw function that display the map on the window

        Args:
            window ([pygame.display]): the current window
            map (map): the class map with all infos from logic part
        """
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
