import graphic.constant as const
from graphic.play import Play
from graphic.main_menu import Main_menu
from graphic.win_menu import Win_menu
from graphic.lose_menu import Lose_menu
import pygame


class Graphic:
    def __init__(self):
        self.status = 0
        pygame.init()
        self.window = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.party = Play()
        self.main_menu = Main_menu()
        self.win_menu = Win_menu()
        self.lose_menu = Lose_menu()
        self.clock = pygame.time.Clock()
        self.done = False

    def event_loop(self, map):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and self.status == const.STATUS_DICT["Win"] or event.type == pygame.KEYDOWN and self.status == const.STATUS_DICT["Lose"]:
                self.done = True

    def gameloop(self, map):
        while not self.done:
            self.clock.tick(const.FPS)
            self.event_loop(map)
            if self.status == const.STATUS_DICT["Main_menu"]:
                self.main_menu.loop(self, self.window)
            if self.status == const.STATUS_DICT["Play"]:
                self.party.loop(self, self.window, map)
            elif self.status == const.STATUS_DICT["Win"]:
                self.win_menu.loop(self, self.window)
            elif self.status == const.STATUS_DICT["Lose"]:
                self.lose_menu.loop(self, self.window)
            pygame.display.flip()
