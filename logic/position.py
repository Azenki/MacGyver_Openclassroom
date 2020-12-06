""" Module of position
"""


class Position:
    """ Class of Position
    """
    def __init__(self, pos):
        """__init__ the position of the item with an int

        Args:
            pos (int): an position of one 15x15 tab
        """
        self.pos = pos
        self.x = pos % 15
        self.y = pos // 15

    def update_x_y(self):
        """update_x_y function that update the x and y position
        from an int position of one 15x15 tab
        """
        self.x = self.pos % 15
        self.y = self.pos // 15

    def print_pos(self):
        """print_pos function that display on the terminal
        the position of the item

        Returns:
            [int]: position of the item, pos is an int of 15x15
            tab, x and y
        """
        return (pos, x, y)
