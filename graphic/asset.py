import pygame

class Asset(pygame.sprite.Sprite):
    def __init__(self, source, rect):
        pygame.sprite.Sprite.__init__(self)
        if rect == None:
            self.rect = source.get_rect()
            self.image = source.subsurface(self.rect)
        else:
            self.image = source.subsurface(rect)
            self.rect = self.image.get_rect()