import pygame

class Map:
    def __init__(self, window, map):
        for i, letter in enumerate(map):
            if letter == 'G':
                pygame.draw.rect(window, "red", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
            elif letter != 'O' and letter != '\n':
                pygame.draw.rect(window, "blue", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
