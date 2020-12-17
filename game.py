import pygame as pg
import sys
from board import Board
from constants import *

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONUP,
)


class Game:
    """
    This class defines the logic of the game and how player input is taken etc
    We run one instance of this class at the start of the game, and this
    instance manages the game for us.
    Attributes:
        width: An integer that represents the width of the display screen.
        height: An integer that represents the height of the display screen.
        display_screen: A PyGame display to view the game.
        new_game: A new instance of the Board class.
        fps: Frames per second.
        clock: Pygame clock to monitor time.
        my_font: Loaded font used to display text on screen.
    """

    def __init__(self):
        """
        Set up a game that creates a new Board instance and assigns groups
        from this instance to the group attributes. Initialize the rest of the
        instance attributes.
        """
        self.display_screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.new_game = Board()
        self.fps = FPS
        self.clock = pg.time.Clock()
        self.my_font = pg.font.Font('slkscr.ttf', 20)

    def runGame(self):
        """
        Run the main loop that displays the board, gets user input,
        and makes changes to the board.
        Since our game goes on infinitely, we have the code that runs the game
        in a while loop that exits only when the player dies.
        """
        self.new_game.reset_groups(0, 9)  # Resets the above groups
        self.new_game.initialize_game()  # Initialize game and generate map
        self.new_game.create_groups()    # Create instance groups
        while True:
            self.clock.tick(self.fps)
            # Display the score and lives on the screen
            self.score_label = self.my_font.render(
                "Score " + str(self.new_game.score), 1, (0, 0, 0))
            self.lives_label = self.my_font.render(
                "Lives: " + str(self.new_game.lives), 1, (0, 0, 0))

            # If the game state is not 2 then redraw screen accordingly and
            # display buttons
            if self.new_game.game_state != 2:

                # Redraw menu screen and buttons
                self.new_game.redraw_screen(
                    self.display_screen,
                    self.score_label,
                    self.lives_label,
                    self.new_game.width,
                    self.new_game.height)

                # Create buttons hover effects
                self.new_game.check_button()

                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEBUTTONUP:
                        # Check which button was clicked and change game state
                        # accordingly
                        if self.new_game.game_state == 1:
                            self.new_game.select_cat()
                        else:
                            self.new_game.process_button()

            # If game state is 2 then run the game:
            if self.new_game.game_state == 2:
                # Create fireballs
                self.new_game.create_fireball()

                self.wallsCollidedAbove = self.new_game.RefCats.check_collision(
                    self.new_game.platform_group)

                # In a PyGame event loop, check which key is being pressed:
                for event in pg.event.get():
                    # If QUIT, Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                # Get the keys that are pressed by the player
                keys = pg.key.get_pressed()

                # Set front facing cat as the defualt image when no key is
                # pressed
                image = f'Cat Images/{self.new_game.Chosen_cat}front.png'

                # Set up the reference image of the cat as image2
                image2 = 'Object Images/referencecat.png'

                # Moving the player to the right if the right arrow key is
                # pressed
                if keys[K_RIGHT]:
                    # Check for collisions between cat reference image and
                    # ladder and platform reference images
                    reference_platforms_collided = self.new_game.RefCats.\
                        check_collision(self.new_game.ref_platform_group)
                    reference_ladders_collided = self.new_game.Players.\
                        check_collision(self.new_game.ref_ladder_group)

                    # Check for collisions between cat reference image and
                    # ladder and platform images
                    ladders_collided = self.new_game.RefCats.check_collision(
                        self.new_game.ladder_group)
                    platforms_collided = self.new_game.RefCats.check_collision(
                        self.new_game.platform_group)

                    # Load image of the cat facing right
                    image = f'Cat Images/{self.new_game.Chosen_cat}right.png'

                    # Make sure the sprite does not move past the edge
                    # of the board
                    if self.new_game.Players.get_position()[
                            0] <= self.new_game.width - 5:
                        # Move the reference and player's position to
                        # the right if the reference is touching the
                        # platform
                        if reference_platforms_collided != []:
                            self.new_game.Players.update_position(pg.image.load(
                                image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                        # Make the player bouce to the right if its at the top
                        # of the ladder
                        if ladders_collided == [] \
                           and reference_ladders_collided != []:
                            self.new_game.Players.update_position(pg.image.load(
                                image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                        # Let the player move right when it is in free fall
                        if platforms_collided == [] and ladders_collided == []:
                            self.new_game.Players.update_position(pg.image.load(
                                image), -self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                # Moving the player to the left if the left key is pressed
                if keys[K_LEFT]:
                    # Check for collisions between cat reference image and
                    # ladder and platform reference images
                    reference_platforms_collided = self.new_game.RefCats.\
                        check_collision(self.new_game.ref_platform_group)
                    reference_ladders_collided = self.new_game.Players.\
                        check_collision(self.new_game.ref_ladder_group)

                    # Check for collisions between cat reference image and
                    # ladder and platform images
                    ladders_collided = self.new_game.RefCats.check_collision(
                        self.new_game.ladder_group)
                    platforms_collided = self.new_game.RefCats.check_collision(
                        self.new_game.platform_group)

                    # Load image of the cat facing left
                    image = f'Cat Images/{self.new_game.Chosen_cat}left.png'

                    # Make sure the sprite does not move past the edge
                    # of the board
                    if self.new_game.Players.get_position()[0] >= 5:
                        # Move the reference and player's position to
                        # the right if the reference is touching the
                        # platform
                        if reference_platforms_collided != []:
                            self.new_game.Players.update_position(pg.image.load(
                                image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                        # Make the player bouce to the right if its at the top
                        # of the ladder
                        if ladders_collided == [] \
                           and reference_ladders_collided != []:
                            self.new_game.Players.update_position(pg.image.load(
                                image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                        # Let the player move right when it is in free fall
                        if platforms_collided == [] and ladders_collided == [
                        ] and self.new_game.Players.get_position()[0] >= 5:
                            self.new_game.Players.update_position(pg.image.load(
                                image), self.new_game.Players.get_speed(), 'H')
                            self.new_game.RefCats.update_position_cat(
                                pg.image.load(image2),
                                self.new_game.Players.get_position())

                # Moving the player down if the down key is pressed
                if keys[K_DOWN]:
                    # Load image of the cat facing forward
                    image = f'Cat Images/{self.new_game.Chosen_cat}front.png'
                    # Move the player slightly downward,
                    # Check for collisions with the reference ladder group
                    # and moving the player back up to its original position
                    self.new_game.Players.update_position(
                        pg.image.load(image), -5, 'V')
                    self.new_game.RefCats.update_position_cat(
                        pg.image.load(image2),
                        self.new_game.Players.get_position())
                    reference_ladders_collided_down = self.new_game.RefCats.\
                        check_collision(self.new_game.ref_ladder_group)
                    self.new_game.Players.update_position(
                        pg.image.load(image), 5, 'V')
                    self.new_game.RefCats.update_position_cat(
                        pg.image.load(image2),
                        self.new_game.Players.get_position())

                    # If the player is on a ladder and not at the
                    # bottom of the screen, it can move downward
                    if reference_ladders_collided_down != [] and \
                            self.new_game.Players.get_position()[1] \
                            <= self.new_game.height - 10:
                        self.new_game.Players.update_position(pg.image.load(
                            image), -self.new_game.Players.get_speed(), 'V')
                        self.new_game.RefCats.update_position_cat(
                            pg.image.load(image2),
                            self.new_game.Players.get_position())

                # Moving the player up if the up key is pressed
                if keys[K_UP]:
                    # Load image of the cat facing up
                    image = f'Cat Images/{self.new_game.Chosen_cat}up.png'
                    # Check for collisions between the ladder reference
                    # and the player reference.
                    ladders_collided = self.new_game.RefCats.check_collision(
                        self.new_game.ladder_group)
                    # If the cat collides with the ladder then it
                    # can move upwards
                    if ladders_collided != []:
                        self.new_game.Players.update_position(pg.image.load(
                            image), self.new_game.Players.get_speed(), 'V')
                        self.new_game.RefCats.update_position_cat(
                            pg.image.load(image2),
                            self.new_game.Players.get_position())
                    # If the player has reached the tope of the
                    # screen, update level
                    if self.new_game.Players.get_position()[1] <= 30:
                        self.new_game.update_level(
                            self.new_game.score, self.new_game.lives)

                # Check for collisions with the ladders
                ladders_collided = self.new_game.RefCats.check_collision(
                    self.new_game.ladder_group)

                # Check for collisions with platform endcaps
                reference_ends_collided = self.new_game.RefCats.check_collision(
                    self.new_game.ref_endcap_group)

                # Move the reference and the player slightly downward,
                # checking for collisions with the platform group
                # and move the player back up to its original position
                self.new_game.Players.update_position(
                    pg.image.load(image), -5, 'V')
                self.new_game.RefCats.update_position_cat(
                    pg.image.load(image2), self.new_game.Players.get_position())
                platforms_collided_down = self.new_game.RefCats.check_collision(
                    self.new_game.platform_group)
                self.new_game.Players.update_position(
                    pg.image.load(image), 5, 'V')
                self.new_game.RefCats.update_position_cat(
                    pg.image.load(image2),
                    self.new_game.Players.get_position())

                # If the player is not colliding with anything then
                # simulate gravity and make the player fall
                if ladders_collided == [] and platforms_collided_down == [
                ] and self.new_game.Players.get_position()[1] <= \
                        self.new_game.height - 10:
                    self.new_game.Players.update_position(
                        pg.image.load(image),
                        -self.new_game.Players.get_speed() * 1.2, 'V')
                    self.new_game.RefCats.update_position_cat(
                        pg.image.load(image2),
                        self.new_game.Players.get_position())

                # If the player collides with an endcap check to see
                # if it collided to the right or left
                if reference_ends_collided:

                    # Check to the right
                    # Move cat
                    self.new_game.Players.update_position(
                        pg.image.load(image), -2, 'H')
                    # Get walls that player has collided with
                    walls_collided_right = self.new_game.RefCats.\
                        check_collision(self.new_game.platform_group)
                    # Move cat back
                    self.new_game.Players.update_position(
                        pg.image.load(image), 2, 'H')

                    # Check to the left
                    # Move cat
                    self.new_game.Players.update_position(
                        pg.image.load(image), 2, 'H')
                    # Get walls that player has collided with
                    walls_collided_left = self.new_game.RefCats.\
                        check_collision(self.new_game.platform_group)
                    # Move cat back
                    self.new_game.Players.update_position(
                        pg.image.load(image), -2, 'H')

                    # If it collided to the right, then move
                    # the player to the left
                    if walls_collided_right:
                        # Update cat position
                        self.new_game.Players.update_position(
                            pg.image.load(image), 10, 'H')
                        # Update cat reference position
                        self.new_game.RefCats.update_position_cat(
                            pg.image.load(image2),
                            self.new_game.Players.get_position())

                    # If it collided to the left, then move
                    # the player to the right
                    if walls_collided_left:
                        # Update cat position
                        self.new_game.Players.update_position(
                            pg.image.load(image), -10, 'H')
                        # Update cat reference position
                        self.new_game.RefCats.update_position_cat(
                            pg.image.load(image2),
                            self.new_game.Players.get_position())

                # Use cycles to animate the stars
                # Decrease cycle_rate to decrease the speed of star animation
                cycle_rate = 48
                cycle = cycle_rate / 6
                path = 'Object Images/star_rot'
                self.new_game.cycles = (self.new_game.cycles + 1) % cycle_rate
                if 1 <= self.new_game.cycles <= cycle:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(
                            'Object Images/yellow star.png'))
                elif cycle + 1 <= self.new_game.cycles <= cycle * 2:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(f'{path}1.png'))
                elif cycle * 2 + 1 <= self.new_game.cycles <= cycle * 3:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(f'{path}2.png'))
                elif cycle * 3 + 1 <= self.new_game.cycles <= cycle * 4:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(f'{path}3.png'))
                elif cycle * 4 + 1 <= self.new_game.cycles <= cycle * 5:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(f'{path}4.png'))
                else:
                    for star in self.new_game.Stars:
                        star.update_image(pg.image.load(f'{path}5.png'))

                # Redraw all instances onto the screen
                self.new_game.redraw_screen(self.display_screen,
                                            self.score_label, self.lives_label,
                                            self.new_game.width,
                                            self.new_game.height)

                # Update the fireball and check for collisions with player.
                self.new_game.fireball_check()

                # Check for star collection
                stars_collected = pg.sprite.spritecollide(
                    self.new_game.Players, self.new_game.star_group, True)
                self.new_game.star_check(stars_collected)

            # Update the display to view changes
            pg.display.update()
