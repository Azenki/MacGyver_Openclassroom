import graphic.constant as const
from graphic.play import Play
from graphic.main_menu import Main_menu
from graphic.pause_menu import Pause_menu
from graphic.win_menu import Win_menu
from graphic.lose_menu import Lose_menu
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class Graphic:
    def __init__(self):
        self.status = 0
        pygame.init()
        self.window = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.party = Play()
        self.main_menu = Main_menu()
        self.pause_menu = Pause_menu()
        self.win_menu = Win_menu()
        self.lose_menu = Lose_menu()
        self.clock = pygame.time.Clock()
        self.done = False

    def event_loop(self, map):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and self.status == const.STATUS_DICT["Win"] or event.type == pygame.KEYDOWN and self.status == const.STATUS_DICT["Lose"]:
                self.done = True
            if self.status == const.STATUS_DICT["Main_menu"]:
                self.main_menu.event(self, keys)
            elif self.status == const.STATUS_DICT["Pause_menu"]:
                self.pause_menu.event(self, keys)
            elif self.status == const.STATUS_DICT["Play"]:
                self.party.event(self, keys, map)

    def draw(self, map):
        if self.status == const.STATUS_DICT["Main_menu"]:
            self.main_menu.draw(self.window)
        elif self.status == const.STATUS_DICT["Pause_menu"]:
            self.pause_menu.draw(self.window)
        elif self.status == const.STATUS_DICT["Play"]:
            self.party.draw(map, self.window)

    def gameloop(self, map):
        while not self.done:
            self.clock.tick(const.FPS)
            self.event_loop(map)
            if self.status == const.STATUS_DICT["Play"]:
                self.party.player.move(map, self)
            elif self.status == const.STATUS_DICT["Win"]:
                self.win_menu.loop(self, self.window)
            elif self.status == const.STATUS_DICT["Lose"]:
                self.lose_menu.loop(self, self.window)
            self.draw(map)
            pygame.display.flip()
