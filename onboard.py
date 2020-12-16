import pygame as pg
import random
import math


class OnBoard(pg.sprite.Sprite):
    """
    Creating an overarching class that defines all the inanimate
    objects in the game like the ladder and the gems. This class
    will set up the position and image from all the inherited
    classes.

    Attributes:
        _position: A tuple representing coordinates.
        image: A string representing the path to a png.
        rect: A tuple representing the dimensions of an image.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes.

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing coordinates of the position.
        """
        super().__init__()
        # Create attributes for the image and the position
        self._position = position
        self.image = raw_image
        # Set the rect attribute to be the image
        self.rect = self.image.get_rect()
        # Set the center of the rect atrribute as the position
        self.rect.center = self._position

    def get_position(self):
        """
        Get the position of the sprite

        Return:
            self._position: The position of the sprite.
        """
        return self._position

    def set_position(self, position):
        """
        Set the position of the object.

        Args:
            position: A tuple representing the position
            of the sprite on the board.
        """
        self._position = position


class Platform(OnBoard):
    """
    Defining all the platforms in the game. This class inherits
    from the OnBoard parent class.

    Attributes:
        position: A tuple representing coordinates.
        image: A string representing the path to a png.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        super().__init__(raw_image, position)


class Ladder(OnBoard):
    """
    Defining all the ladders in the game. This class inherits
    from the OnBoard parent class.

    Attributes:
        position: A tuple representing coordinates.
        image: A string representing the path to a png.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the ladder.
        """
        # Use super to call the attributes from the parent OnBoard class.
        super().__init__(raw_image, position)


class Fireball(OnBoard):
    """
    Creates all the fireballs for the board that
    fall down the screen. Checks whether the player collides
    with these fireballs or not. This class inherits from the
    OnBoard parent class.

        Attributes:
            position: The position of the image
            image: The image file for that object
            index: A number that uniquely identifies every fireball
            speed: The speed of the fireball
            fall: A 0 for if the fireball is not falling and a 1 if it is.
    """

    def __init__(self, raw_image, position, index, speed):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing coordinates of
            the position.
            index: An integer that uniquely identifies each fireball
            speed: An integer that sets the speed of the fireball.
        """
        super().__init__(raw_image, position)
        self.index = index
        # The newly spawned fireball is not falling
        self._fall = 0
        # The speed of a fireball is set
        self._speed = speed

    def get_fall(self):
        # Return the index 1 or 0 for falling or not falling
        return self._fall

    def update(self, raw_image, speed):
        """
        Moving the fireball downwards in the based on an input value.

        Attributes:
            raw_image: A fireball image file
            speed: The speed at which the fireball moves.
        """
        # Move the fireball in the required direction with
        # the required value and also set the image of the fireball
        self.set_position((self.get_position()[0],
                           self.get_position()[1] - speed))
        self.rect.center = self.get_position()

    def check_collision(self, collider_group):
        """
        Checking to see if the fireball collides with the player.

        Args:
            collider_group: A pygame group that the
            which contains instances of a specific object.

        Returns:
            Colliders: An empty or filled list which tells it whether
            it collides with a group or not.
        """
        # Use the pygame sprite collider to check if there is a collison
        # between the sprite and the player
        self.update(self.image, self._speed)  # Bottom collision
        colliders = pg.sprite.spritecollide(self, collider_group, True)
        return colliders

    def continuous_update(self, collider_group):
        """
        Continously updating the fireball.

        Args:
            collider_group: A pygame group that the
            fireball collides with
        """
        # Set the fireball as falling
        # Update the position of the fireball
        if self._fall == 1:
            # We move the fireball downwards with speed of self.__speed
            self.update(self.image, self._speed)
            if self.check_collision(collider_group):
                # If the fireball collides with a group
                # then it stops falling
                self._fall = 0


class Star(OnBoard):
    """
    Defining all the stars in the game. This class inherits
    from the OnBoard class. The stars increase the player score.

    Attributes:
        position: A tuple representing the coordinates of a star.
        image: A string representing the path to a png.
    """

    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes.

        Args:
            raw_image: A ladder image file.
            position: A tuple representing coordinates of
            the position.
        """
        # Use super to call the attributes from the parent OnBoard class.
        # Initialize the value attribute as some integer.
        super().__init__(raw_image, position)
        self.image = pg.transform.scale(self.image, (20, 20))

    def update_image(self, raw_image):
        """
        Update the star image.

        Args:
            raw_image: A string representing the path to a png.
        """
        self.image = raw_image
        self.image = pg.transform.scale(self.image, (20, 20))


class Boundary(OnBoard):
    """
    Defining all the boundaries in the game. This class inherits
    from the OnBoard class.
    """
    def __init__(self, raw_image, position):
        """
        Initialize the image, position and rect instance attributes

        Args:
            raw_image: A string representing the path to a png.
            position: A tuple representing the coordinates of
            the platform.
        """
        super().__init__(raw_image, position)
        self.image = raw_image
