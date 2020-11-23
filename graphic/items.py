import pygame
from graphic.asset import Asset
import graphic.constant


class Items:
    def __init__(self):
        self.SYRINGE_RESIZE = pygame.transform.scale(graphic.constant.SYRINGE_IMG, (32, 32))
        self.TUBE_RESIZE = pygame.transform.scale(graphic.constant.TUBE_IMG, (32, 32))
        self.SYRINGE_RESIZE.convert_alpha()
        self.syringe = Asset(self.SYRINGE_RESIZE, self.SYRINGE_RESIZE.get_rect())
        self.tube = Asset(self.TUBE_RESIZE, self.TUBE_RESIZE.get_rect())
    
    def draw(self,window, map):
        item_one = 0
        item_two = 0
        for i, letter in enumerate(map):
            x = i % 15 * 32
            y = i // 15 * 32
            if letter == '0':
                self.syringe.rect.x = x
                self.syringe.rect.y = y
                window.blit(self.syringe.image, self.syringe.rect)
                item_one = 1
            elif letter == '1':
                self.tube.rect.x = x
                self.tube.rect.y = y
                window.blit(self.tube.image, self.tube.rect)
                item_two = 1
        if item_one == 0:
            self.syringe.rect.x = 490
            self.syringe.rect.y = 10
            window.blit(self.syringe.image, self.syringe.rect)
        if item_two == 0:
            self.tube.rect.x = 490
            self.tube.rect.y = 52
            window.blit(self.tube.image, self.tube.rect)