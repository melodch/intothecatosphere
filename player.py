import pygame as pg
from constants import *


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
        super(Person, self).__init__()
        self.__position = position
        self.image = image
        self.image = pg.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = self._position

    def set_center(self, position):
        """
        Set the center of the person's image to the position.
        """
        self.rect.center = position

    def get_position(self):
        """
        Get the coordinates of the person.
        """
        return self._position

    def set_position(self, position):
        """
        Set the position of the person.
        """
        self._position = position

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

    
    def update_position(self, raw_image, value, direction):
        if direction == 'V'
            self._position = (self._position[0], self._position[1] + value)
        if direction == 'H'
            self._position = (self._position[0] + value, self._position[1])
        self.rect.center = self._position

    def check_collision(self, colliderGroup):
        colliders = pg.sprite.spritecollide(self, colliderGroup, False)
        return colliders

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
        super(Player, self).__init__(raw_image, position)
        self.onLadder = 0
        self.__gravity = 1  # Gravity affecting the jump velocity of the player
        self.__speed = 5  # Movement speed of the player

    def get_speed(self):
        """
        Get the player speed.

        Returns:
            An integer representing the player's movement speed.
        """
        return self.__speed

    def set_speed(self, speed):
        """
        Set the player movement speed.
        """
        self.__speed = speed


class PlayerView(Player):
    """
    An object inheriting from the Player class, representing the
    character's view. This updates every time the player moves.
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
