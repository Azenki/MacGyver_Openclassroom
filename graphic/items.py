import pygame
from graphic.asset import Asset
import graphic.constant


class Items:
    def __init__(self):
        self.list_of_item = []
        self.SYRINGE_RESIZE = pygame.transform.scale(graphic.constant.SYRINGE_IMG, (32, 32))
        self.TUBE_RESIZE = pygame.transform.scale(graphic.constant.TUBE_IMG, (32, 32))
        self.SYRINGE_RESIZE.convert_alpha()
        self.syringe = Asset(self.SYRINGE_RESIZE, self.SYRINGE_RESIZE.get_rect())
        self.tube = Asset(self.TUBE_RESIZE, self.TUBE_RESIZE.get_rect())
        self.list_of_item.append(self.tube)
        self.list_of_item.append(self.syringe)
        self.list_of_item.append(self.tube)
        self.list_of_item.append(self.syringe)
    
    def draw(self,window, map):
        for i, item in enumerate(map.list_of_item):
            if item.status == 0:
                self.list_of_item[i].rect.x = item.pos.x * 32
                self.list_of_item[i].rect.y = item.pos.y * 32
                window.blit(self.list_of_item[i].image, self.list_of_item[i].rect)
            else:
                self.list_of_item[i].rect.x = 490
                self.list_of_item[i].rect.y = 10 + i * 37
                window.blit(self.list_of_item[i].image, self.list_of_item[i].rect)