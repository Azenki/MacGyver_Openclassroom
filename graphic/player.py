import pygame
import graphic.constant as const
from graphic.asset import Asset

""" Module of Player
"""


class Player:
    """ Class player that init and draw the player and
    hold his move functions
    """
    def __init__(self):
        """__init__ the player sprite
        """
        self.sprite = Asset(const.PLAYER_IMG, pygame.Rect(0, 0, 32, 32))

    def draw(self, window, pos):
        """draw function that display the player on the window

        Args:
            window ([pygame.display]): the current window
            pos ([position]): position of the guardian
        """
        self.sprite.rect.x = pos % 15 * 32
        self.sprite.rect.y = pos // 15 * 32
        window.blit(self.sprite.image, self.sprite.rect)

    def move(self, map, party):
        """move function that update his position on the map by
        player module from logic part

        Args:
            map ([map class]): the class map with all stuff infos
            party (play): the module contain current game info
        """
        keys = pygame.key.get_pressed()
        map.player.check_end(map, party)
        if keys[pygame.K_RIGHT]:
            map.player.move_right(map.map)
        elif keys[pygame.K_LEFT]:
            map.player.move_left(map.map)
        elif keys[pygame.K_UP]:
            map.player.move_up(map.map)
        elif keys[pygame.K_DOWN]:
            map.player.move_down(map.map)
        map.player.get_item(map)
