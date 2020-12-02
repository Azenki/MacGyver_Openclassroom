import pygame
import graphic.constant
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items


class Play:
    """Class play in graphic in class"""
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.guardian = Guardian()
        self.items = Items()

    def event(self, parent, map):
        keys = pygame.key.get_pressed()
        self.player.move(map, parent)

    def draw(self, map, window):
        """Class play in graphic ijdzaoijfoeziagfiezjipgfe"""
        window.fill("black")
        self.map.draw(window, map.map)
        self.items.draw(window, map)
        self.guardian.draw(window, map.guardian.pos)
        self.player.draw(window, map.player.pos.pos)

    def loop(self, parent, window, map):
        self.event(parent, map)
        self.draw(map, window)
