from onboard import OnBoard
import pygame as pg
from player import Person


class ReferencePlatform(OnBoard):
    """
    Defining all the reference images for the platforms.

    Attributes:
        raw_image: A string representing the path to a png.
        position: A tuple representing the coordinates of
        the image.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes
        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # initializing the position and image
        super().__init__(raw_image, position)


class ReferenceLadder(OnBoard):
    """
    Defining all the reference images for the ladders.

    Attributes:
        raw_image: A string representing the path to a png.
        position: A tuple representing the coordinates of
        the image.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes
        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
                the ladder.
        """
        # initializing the position and image
        super().__init__(raw_image, position)


class ReferenceEndcap(OnBoard):
    """
    Defining all the reference images for the ends of the platforms.

    Attributes:
        raw_image: A string representing the path to a png.
        position: A tuple representing the coordinates of
        the image.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes
        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        # initializing the position and image
        super().__init__(raw_image, position)


class ReferenceCat(Person):
    """
    Defining the reference image for the cat.

    Attributes:
        raw_image: A string representing the path to a png.
        position: A tuple representing the coordinates of
        the image.
    """

    def __init__(self, raw_image, position):
        """
        Initiate a player that inherits from the Person class with a certain
        movement speed.

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple of integers representing coordinates.
        """
        # initializing the position and image
        super().__init__(raw_image, position)

    def update_position_cat(self, raw_image, position):
        """
        Update the position of the reference image for the cat

        Args:
            position: A tuple representing the position of the cat
            raw_image: A string representing the path to a png.

        Return:
            _position: The position of the reference image for the cat.
        """
        self.image = raw_image
        self._position = (position[0] - 2, position[1] + 10)
        self.rect.center = self._position
        return self._position
