import pygame
import graphic.constant
from graphic.asset import Asset

class Player:
    def __init__(self):
        self.sprite = Asset(graphic.constant.PLAYER_IMG, pygame.Rect(0, 0, 32, 32))
    
    def draw(self, window, pos):
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)
    
    def move(self, map):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            map.player.move_right(map.map)
        elif keys[pygame.K_LEFT]:
            map.player.move_left(map.map)
        elif keys[pygame.K_UP]:
            map.player.move_up(map.map)
        elif keys[pygame.K_DOWN]:
            map.player.move_down(map.map)
        map.player.get_item(map)