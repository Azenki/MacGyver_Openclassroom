import pygame
from graphic.asset import Asset
import graphic.constant as const


class Items:
    def __init__(self):
        self.list_of_item = []
        self.list_of_source = [const.SYRINGE_IMG, const.ETHER_IMG, const.TUBE_IMG, const.NEEDLE_IMG]
        for i in range(0, 4):
            item = Asset(self.list_of_source[i], pygame.Rect(0, 0, 32, 32))
            self.list_of_item.append(item)

    def draw(self, window, map):
        for i, item in enumerate(map.list_of_item):
            if item.status == 0:
                self.list_of_item[i].rect.x = item.pos.x * 32
                self.list_of_item[i].rect.y = item.pos.y * 32
                window.blit(self.list_of_item[i].image, self.list_of_item[i].rect)
            else:
                self.list_of_item[i].rect.x = 490
                self.list_of_item[i].rect.y = 10 + i * 37
                window.blit(self.list_of_item[i].image, self.list_of_item[i].rect)
