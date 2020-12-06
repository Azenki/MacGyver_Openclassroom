import pygame
import graphic.constant as const
from graphic.asset import Asset

""" Module of the guardian
"""


class Guardian:
    """ class Guardian, init and draw the guardian sprite
    """
    def __init__(self):
        """__init__ the guardian sprite
        """
        self.sprite = Asset(const.GUARDIAN_IMG, pygame.Rect(0, 0, 32, 32))

    def draw(self, window, pos):
        """draw function that display the guardian on the window

        Args:
            window ([pygame.display]): the current window
            pos ([position]): position of the guardian
        """
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)
