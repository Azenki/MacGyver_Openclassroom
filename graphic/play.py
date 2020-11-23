import pygame
import graphic.constant
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items

class Play:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.guardian = Guardian()
        self.items = Items()
    def event(self, parent, keys, map):
        if keys[pygame.K_ESCAPE]:
                parent.status = graphic.constant.STATUS_DICT["Pause_menu"]
    def draw(self, map, window):
        window.fill("black")
        self.map.draw(window, map.map)
        self.items.draw(window, map)
        self.guardian.draw(window, map.guardian.pos)
        self.player.draw(window, map.player.pos.pos)