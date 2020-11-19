import pygame
import os
from os.path import dirname, abspath
from graphic.asset import Asset

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
SPRITE_SHEET = pygame.image.load(os.path.join(IMG_FOLDER, "[32x32]Dungeon_Bricks_Shadow.png"))

class Map:
    def __init__(self):
        self.wall = Asset(SPRITE_SHEET, pygame.Rect(96, 0, 32, 32))
        self.road = Asset(SPRITE_SHEET, pygame.Rect(32, 32, 32, 32))

    def draw(self, window, map):
        for i, letter in enumerate(map):
            x = i % 15 * 32
            y = i // 15 * 32
            if letter == 'O':
                self.wall.rect.x = x
                self.wall.rect.y = y
                window.blit(self.wall.image, self.wall.rect)
            else:
                self.road.rect.x = x
                self.road.rect.y = y
                window.blit(self.road.image, self.road.rect)
            
        
        
