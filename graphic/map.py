import pygame

class Map:
    def __init__(self, window, map):
        for i, letter in enumerate(map):
            if letter == 'P':
                pygame.draw.rect(window, "green", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
            elif letter == '0' or letter == '1':
                pygame.draw.rect(window, "white", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
            elif letter == 'G':
                pygame.draw.rect(window, "red", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
            elif letter != 'O' and letter != '\n':
                pygame.draw.rect(window, "blue", pygame.Rect(i % 16 * 10 + 10, i // 16 * 10 + 10, 10, 10))
