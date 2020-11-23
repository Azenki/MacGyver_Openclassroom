from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *
from graphic.map import Map
from graphic.player import Player
from graphic.guardian import Guardian
from graphic.items import Items
from graphic.menu import Main_menu

WIDTH = 600
HEIGHT = 480
FPS = 10

class Gameboard:
    def __init__(self):
        self.status_dict = {"Main_menu" : 0, "Pause_menu" : 1, "Play" : 2, "Win" : 3, "Lose" : 4}
        self.status = 0
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map()
        self.player = Player()
        self.guardian = Guardian()
        self.items = Items()
        self.main_menu = Main_menu()
        self.clock = pygame.time.Clock()

    def event_loop(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.status == self.status_dict["Main_menu"] and keys[pygame.K_RETURN]:
                self.status = self.status_dict["Play"]
        return False

    def draw_game(self, map):
        self.window.fill("black")
        self.map.draw(self.window, map.map)
        self.items.draw(self.window, map)
        self.guardian.draw(self.window, map.guardian.pos)
        self.player.draw(self.window, map.player.pos.pos)

    def draw_menu(self, map):
        self.main_menu.draw(self.window)

    def check_end(self, map):
        if map.player.pos == map.guardian.pos:
            if '1' in map.map and '0' in map.map:
                print("Lose, see you next time !")
            elif '1' in map.map:
                print("You tried to prick with the syringe but he stoped you first ! You lose.")
            elif '0' in map.map:
                print("You tried to hit him with your tube, you suprised him but he catch you. You lose.")
            else:
                print("You hit him with your tube, you suprised him and pricked it with the seringe and he falls. Congrats, you are free !")
            return True
        else:
            return False

    def draw(self, map):
        if self.status == self.status_dict["Main_menu"]:
            self.draw_menu(map)
        elif self.status == self.status_dict["Pause_menu"]:
            pass
        elif self.status == self.status_dict["Play"]:
            self.draw_game(map)

    def gameloop(self, map):
        done = False
        while not done:
            self.clock.tick(FPS)
            done = self.event_loop()
            self.player.move(map)
            self.draw(map)
            if not done:
                done = self.check_end(map)
            pygame.display.flip()
