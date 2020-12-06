import pygame

""" Module of graphic asset that contains sprite image and position
"""


class Asset(pygame.sprite.Sprite):
    """Class of asset

    Args:
        pygame ([pygame.sprite.Sprite]): pygame arg
    """
    def __init__(self, source, rect):
        """__init__ [summary]

        Args:
            source (pygame.image.load): the image used for the asset
            rect (pygame.rect): infos of the image, size and positions
        """
        pygame.sprite.Sprite.__init__(self)
        if rect is None:
            self.rect = source.get_rect()
            self.image = source.subsurface(self.rect)
        else:
            self.image = source.subsurface(rect)
            self.rect = self.image.get_rect()
