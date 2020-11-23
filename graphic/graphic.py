from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import graphic.constant
from pygame.locals import *
from graphic.play import Play
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items
from graphic.main_menu import Main_menu
from graphic.pause_menu import Pause_menu

class Graphic:
    def __init__(self):
        self.status = 0
        pygame.init()
        self.window = pygame.display.set_mode((graphic.constant.WIDTH, graphic.constant.HEIGHT))
        self.party = Play()
        self.main_menu = Main_menu()
        self.pause_menu = Pause_menu()
        self.clock = pygame.time.Clock()
        self.done = False

    def event_loop(self, map):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if self.status == graphic.constant.STATUS_DICT["Main_menu"]:
                self.main_menu.event(self, keys)
            elif self.status == graphic.constant.STATUS_DICT["Pause_menu"]:
                self.pause_menu.event(self, keys)
            elif self.status == graphic.constant.STATUS_DICT["Play"]:
                self.party.event(self, keys, map)

    def draw(self, map):
        if self.status == graphic.constant.STATUS_DICT["Main_menu"]:
            self.main_menu.draw(self.window)
        elif self.status == graphic.constant.STATUS_DICT["Pause_menu"]:
            self.pause_menu.draw(self.window)
        elif self.status == graphic.constant.STATUS_DICT["Play"]:
            self.party.draw(map, self.window)

    def gameloop(self, map):
        while not self.done:
            self.clock.tick(graphic.constant.FPS)
            self.event_loop(map)
            if self.status == graphic.constant.STATUS_DICT["Play"]:
                self.party.player.move(map)
            self.draw(map)
            """if not done:
                done = self.check_end(map)"""
            pygame.display.flip()
