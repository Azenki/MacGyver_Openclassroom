import pygame
import graphic.constant
from graphic.asset import Asset

""" Module of Win menu
"""


class Win_menu:
    """ Class Win menu, init and draw the win menu
    """
    def __init__(self):
        """__init__ the win menu sprite
        """
        self.sprite = Asset(graphic.constant.WIN_MENU_IMG, None)

    def draw(self, window):
        """draw function that display the win menu on the window

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
