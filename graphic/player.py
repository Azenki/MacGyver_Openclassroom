import pygame
import os
from os.path import dirname, abspath
from graphic.asset import Asset

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
PLAYER_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "MacGyver.png"))

class Player:
    def __init__(self):
        self.sprite = Asset(PLAYER_IMG, pygame.Rect(0, 0, 32, 32))
    
    def draw(self, window, pos):
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)
    
    def move(self, map):
        pos = map.player.pos
        keys = pygame.key.get_pressed()
        if pos % 15 != 14 and keys[pygame.K_RIGHT] and map.map[pos + 1] != "O":
            map.player.pos += 1
        elif pos % 15 != 0 and keys[pygame.K_LEFT] and map.map[pos - 1] != "O":
            map.player.pos -= 1
        elif pos // 15 != 0 and keys[pygame.K_UP] and map.map[pos - 15] != "O":
            map.player.pos -= 15
        elif pos // 15 != 14 and keys[pygame.K_DOWN] and map.map[pos + 15] != "O":
            map.player.pos += 15
        if map.map[map.player.pos] == '0' or map.map[map.player.pos] == '1':
            map.map[map.player.pos] = '*'