import pygame
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items
from graphic.menu import Main_menu

class Play:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.guardian = Guardian()
        self.items = Items()
    def draw(self, map, window):
        window.fill("black")
        self.map.draw(window, map.map)
        self.items.draw(window, map)
        self.guardian.draw(window, map.guardian.pos)
        self.player.draw(window, map.player.pos.pos)