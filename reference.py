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
        super().__init__(raw_image, position)
        self.image = raw_image
        #self.image = pg.transform.scale(self.image, (15,5))

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
                the ladder.
        """
        # boundary problem will fix if the lines are bigger
        super().__init__(raw_image, position)
        self.image = raw_image
        #self.image = pg.transform.scale(self.image, (3,26))

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
        super().__init__(raw_image, position)
        self.image = raw_image


class ReferenceCat(Person):
    """
    Defining all the platforms in the game.
    """
    """
    A class that defines the player. A player is a person specialized with a
    movement speed. Separation of the Person and Player classes allows for
    more sustainable customization in the future.

    Attributes:
        _speed: An integer representing the movement speed of the player.
    """

    def __init__(self, raw_image, position):
        """
        Initiate a player that inherits from the Person class with a certain
        movement speed.

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple of integers representing coordinates.
        """
        super().__init__(raw_image, position)
        self._position = position
        self.onLadder = 0
        self.__gravity = 1  # Gravity affecting the jump velocity of the player
        self.__speed = 5  # Movement speed of the player
        self.image = raw_image
        

    def update_position_cat(self, raw_image, position):
        #self.image = raw_image

        self.image = raw_image
        self._position = (position[0] - 2 , position[1] + 10)
        self.rect.center = self._position
        return self._position  