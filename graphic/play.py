import pygame
import graphic.constant
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items

""" Module of Play
"""


class Play:
    """ Class Play create a party of the game, init a new gameboard with all stuff
    """
    def __init__(self):
        """__init__ init the map, player, guardian and items
        """
        self.map = Map()
        self.player = Player()
        self.guardian = Guardian()
        self.items = Items()

    def event(self, parent, map):
        """event [summary]

        Args:
            parent ([graphic class]): the parent class with windows info
            map ([map class]): the class map with all stuff infos
        """
        keys = pygame.key.get_pressed()
        self.player.move(map, parent)

    def draw(self, map, window):
        """draw [summary]

        Args:
            map ([type]): [description]
            window ([type]): [description]
        """
        window.fill("black")
        self.map.draw(window, map.map)
        self.items.draw(window, map)
        self.guardian.draw(window, map.guardian.pos)
        self.player.draw(window, map.player.pos.pos)

    def loop(self, parent, window, map):
        self.event(parent, map)
        self.draw(map, window)
