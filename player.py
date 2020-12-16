import pygame as pg


class Person(pg.sprite.Sprite):
    """
    This class defines all 'living' objects in the game. These objects
    are capable of climbing ladders, moving horizontally and falling.

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
        super().__init__()
        # Create attributes for the image and the position
        self._position = position
        self.image = image
        # Sets the rect attribute to be the image
        self.rect = self.image.get_rect()
        self.rect.center = self._position

    def set_center(self, position):
        """
        Set the center of the person's image to the position.

        Args:
            A tuple representing a position on the board
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

        Args:
            A tuple representing a position on the board
        """
        self._position = position

    def update_position(self, raw_image, speed, direction):
        """
        Update the players position based on the direction its
        moving in.

        Args:
            raw_image: A string representing the path to a png.
            speed: An integer representing the speed of the player.
            direction: A string which is H or V depending on whether
            the movement is horizantal or vertical respectively.
        """
        # intializes the image again so that it can be changed
        # based on whether player is moving right, left up or down
        self.image = raw_image
        # if the player is moving vertically, change the y value
        # of the position based on the input value
        if direction == 'V':
            self._position = (self._position[0], self._position[1] - speed)
        # if the player is moving horizantally, change the x value
        # of the position based on the input value
        if direction == 'H':
            self._position = (self._position[0] - speed, self._position[1])
        self.rect.center = self._position

    def check_collision(self, collider_group):
        """
        Check for collisions between the player and the input
        collider group which can be ladders, platforms or fireballs.

        Args:
            collider_group: A pygame sprite group
        """
        colliders = pg.sprite.spritecollide(self, collider_group, False)
        return colliders


class Player(Person):
    """
    A class that defines the player. A player is a person specialized with a
    movement speed. Separation of the Person and Player classes allows for
    more sustainable customization in the future.

    Attributes:
        image: A string representing the path to a png.
         _position: A tuple of integers representing coordinates of the person.
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
        self._speed = 5  # Movement speed of the player

    def get_speed(self):
        """
        Get the player speed.

        Returns:
            An integer representing the player's movement speed.
        """
        return self._speed

    def set_speed(self, speed):
        """
        Set the player movement speed.

        Args:
            An intger representing the players movement speed.
        """
        self._speed = speed
