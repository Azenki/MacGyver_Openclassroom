import pygame
import graphic.constant
from graphic.asset import Asset

""" Module of the lose menu
"""


class Lose_menu:
    """ Class Lose menu, init and draw the lose menu
    """
    def __init__(self):
        """__init__ the lose menu sprite
        """
        self.sprite = Asset(graphic.constant.LOSE_MENU_IMG, None)

    def draw(self, window):
        """draw function that display the lose menu on the window

        Args:
            window ([pygame.display]): the current window
        """
        window.blit(self.sprite.image, self.sprite.rect)

    def loop(self, parent, window):
        """loop

        Args:
            parent ([graphic]): the graphic module contain all graphic stuff
            window ([pygame.display]): the current window
        """
        self.draw(window)
