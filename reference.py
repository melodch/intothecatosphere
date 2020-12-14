from onboard import OnBoard
import pygame as pg
from player import Person

class ReferencePlatform(OnBoard):
    """
    Defining all the platforms in the game.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # boundary problem will fix if the lines are bigger
        super(ReferencePlatform, self).__init__(raw_image, position)
        self.image = raw_image
        self.image = pg.transform.scale(self.image, (15,5))

class ReferenceLadder(OnBoard):
    """
    Defining all the platforms in the game.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # boundary problem will fix if the lines are bigger
        super(ReferenceLadder, self).__init__(raw_image, position)
        self.image = raw_image
        self.image = pg.transform.scale(self.image, (3,5))

class ReferenceEndcap(OnBoard):
    """
    Defining all the platforms in the game.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # boundary problem will fix if the lines are bigger
        super(ReferenceEndcap, self).__init__(raw_image, position)
        self.image = raw_image


class ReferenceCat(Person):
    """
    Defining all the platforms in the game.
    """
    def __init__(self, image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # boundary problem will fix if the lines are bigger
        super(ReferenceCat, self).__init__(image, position)
        self.image = image
        self.image = pg.transform.scale(self.image, (15,5))
