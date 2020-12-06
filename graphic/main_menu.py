import pygame
import graphic.constant
from graphic.asset import Asset

""" Module of Main menu
"""


class Main_menu:
    """ Class Main menu, init and draw the main menu
    """
    def __init__(self):
        """__init__ the main menu sprite
        """
        self.sprite = Asset(graphic.constant.MAIN_MENU_IMG, None)

    def event(self, parent):
        """event of the main menu

        Args:
            parent ([graphic]): the graphic module contain all graphic stuff
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            parent.status = graphic.constant.STATUS_DICT["Play"]
        if keys[pygame.K_ESCAPE]:
            parent.done = True

    def draw(self, window):
        """draw function that display the main menu on the window

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
        self.event(parent)
        self.draw(window)
