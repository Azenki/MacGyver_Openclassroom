from logic.position import Position
import graphic.constant as const

""" Module of Player
"""


class Player:
    """ Class of Player with his info and movement functions
    """
    def __init__(self, pos):
        """__init__ the player position

        Args:
            pos (int): position of the item
        """
        self.pos = Position(pos)

    def move_left(self, map):
        """move_left function make the player move to the left

        Args:
            map (map): the map class with all the info of the map
        """
        if self.pos.pos % 15 != 0 and map[self.pos.pos - 1] != 'O':
            self.pos.pos -= 1

    def move_right(self, map):
        """move_right function make the player move to the right

        Args:
            map (map): the map class with all the info of the map
        """
        if self.pos.pos % 15 != 14 and map[self.pos.pos + 1] != "O":
            self.pos.pos += 1

    def move_up(self, map):
        """move_up function make the player move to the top

        Args:
            map (map): the map class with all the info of the map
        """
        if self.pos.pos // 15 != 0 and map[self.pos.pos - 15] != 'O':
            self.pos.pos -= 15

    def move_down(self, map):
        """move_down function make the player move to the bottom

        Args:
            map (map): the map class with all the info of the map
        """
        if self.pos.pos // 15 != 14 and map[self.pos.pos + 15] != 'O':
            self.pos.pos += 15

    def get_item(self, map):
        """get_item function that put item on the map to the inventory

        Args:
            map (map): the map class with all the info of the map
        """
        for item in map.list_of_item:
            if self.pos.pos == item.pos.pos:
                item.status = 1

    def check_end(self, map, party):
        """check_end function that check if the player is on the goal
        position and define the end

        Args:
            map (map): the map class with all the info of the map
            party (play): the module contain current game info
        """
        if self.pos.pos == map.guardian.pos:
            for item in map.list_of_item:
                if item.status == 0:
                    party.status = const.STATUS_DICT["Lose"]
                    return
            party.status = const.STATUS_DICT["Win"]
