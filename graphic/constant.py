import os
import pygame
from os.path import dirname, abspath

GAME_FOLDER = dirname(dirname(abspath(__file__)))
IMG_FOLDER = os.path.join(GAME_FOLDER, "ressource")
SYRINGE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "seringue.png"))
TUBE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "tube_plastique.png"))
GUARDIAN_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "Gardien.png"))
PLAYER_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "MacGyver.png"))
NEEDLE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "aiguille.png"))
ETHER_IMG = pygame.image.load(os.path.join(IMG_FOLDER, "ether.png"))