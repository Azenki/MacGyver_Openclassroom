from logic.position import Position

""" Module of Item
"""


class Item:
    """ Class of items with their status on the map or not and their positions
    """
    def __init__(self, pos):
        """__init__ the item with his status and position on the map

        Args:
            pos (int): position of the item
        """
        self.status = 0
        self.pos = Position(pos)
