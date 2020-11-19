import pygame

class Asset(pygame.sprite.Sprite):
    def __init__(self, source, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = source.subsurface(rect)
        self.rect = self.image.get_rect()
