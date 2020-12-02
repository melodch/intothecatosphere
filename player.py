import pygame as pg
from Constants import *


class Person(pg.sprite.Sprite):
    """
    This class defines all 'living' objects in the game. These objects
    are capable of climbing ladders and moving horizontally.

    Attributes:
        image: A string representing the path to a png.
        rect: A tuple of integers representing the width and height of
              the person.
       _position: A tuple of integers representing coordinates of the person.
    """

    def __init__(self, image, position):
        """
        Initiate a person and process their image into a square. Establish
        their position.

        Args:
            image: A string representing the path to a png.
            position: A tuple of integers representing coordinates.
        """
        pass

    def set_center(self, position):
        """
        Set the center of the person's image to the position.
        """
        pass

    def get_position(self):
        """
        Get the coordinates of the person.
        """
        pass

    def set_position(self, position):
        """
        Set the position of the person.
        """
        pass

    def get_speed(self):
        """
        Abstract method that is implemented in the subclass.
        """
        raise NotImplementedError("Subclass must implement this.")

    def set_speed(self):
        """
        Abstract method that is implemented in the subclass.
        """
        raise NotImplementedError("Subclass must implement this.")


class Player(Person):
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
        pass

    def get_speed(self):
        """
        Get the player speed.

        Returns:
            An integer representing the player's movement speed.
        """
        pass

    def set_speed(self, speed):
        """
        Set the player movement speed.
        """
        pass


class PlayerView(Player):
    """
    An object inheriting from the Player class,
    representing the character's view.
    The view is a circle centered around the player with a certain radius.
    Everything else in the game is in black.

    Attributes:
        radius: An integer representing the radius of the player view.
    """

    def __init__(self):
        """
        Initiate the player view radius.
        """
        pass
