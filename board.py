import pygame as pg
import math
import random
import sys
import time
from constants import WIDTH
from constants import HEIGHT
from onboard import OnBoard
from star import Star
from player import Player
from onboard import Fireball
from button import Button
from onboard import Platform
from onboard import Ladder
from reference import ReferencePlatform
from reference import ReferenceLadder
from reference import ReferenceEndcap
from reference import ReferenceCat


class Board:
    """
    This class defines our gameboard.
    A gameboard contains everthing related to our game on it
    like our player, platforms, ladders, stars, etc.
    Attributes:
        self._width = WIDTH
        self._height = HEIGHT
        self.score = 0          # Initialize player's score
        self.lives = 9          # Initialize player's lives
        self.game_state = 0     # Initialize game state to pregame
        self.cycles = 0         # Used for animation
        self.map = []
        self.myfont = pg.font.Font('slkscr.ttf', 50)
        width: An integer that represents the width of the display screen.
        height: An integer that represents the height of the display screen.
        score: An integer representing the player's score which updates as they
            collect stars.
        lives:
        game_state: An integer that represents the state of the game,
            (where 0 is pre-game, 1 is game, and 2 is post-game).
        map: A list of lists representing a 2D array to keep track of the
            positions of the game componenets on screen
            (where 1 represents a platform, 2 ladder, and 3 star).
        h_spacing: Vertcial spacing between platforms.
        Players: A list of Player instances on screen.
        Stars: A list of Star instances on screen.
        Platforms: A list of Platform instances on screen.
        Ladders: A list of Ladder instances on screen.
        ReferencePlatforms: A list of ReferencePlatform instances on screen.
        ReferenenceLadders: A list of ReferenceLadder instances on screen.
        ReferenceEndcaps: A list of ReferenceEndcap instances on screen.
        ReferenceCats: A list of ReferenceCat instances on screen.
        Fireballs: A list of Fireball instances on screen.
        Buttons: A list of Button instances that represent on-screen buttons
            to be pressed (for start, restart and exit).
        Active_buttons: A list of 0s and 1s that represent which buttons are
            being used on screen.
        Cat_buttons: A list of Button instances that represent on-screen buttons
            to be pressed (for cat selection).
        fireball_group: A PyGame group that contains Fireball instances.
        player_group: A PyGame group that contains Player instances.
        platform_group: A PyGame group that contains Platform instances.
        ladder_group: A PyGame group that contains Ladder instances.
        star_group: A PyGame group that contains star instances to be displayed.
        ref_platform_group: A PyGame group that contains
            ReferencePlatform instances.
        ref_ladder_group: A PyGame group that contains
            ReferenceLadder instances.
        ref_endcap_group: A PyGame group that contains
            ReferenceEndcap instances.
        ref_cat_group: A PyGame group that contains ReferenceCat instances.
    """

    def __init__(self):
        """
        Set up a board that connects and initializes all aspects of our game
        as instance variables.
        """
        # Create the buttons used in the pregame and postgame screens.
        self.Buttons = [
            Button(pg.image.load('Object Images/start_meow.png'),
                   (140, 320), "start"),
            Button(pg.image.load('Object Images/exit_game.png'),
                   (360, 320), "exit"),
            Button(pg.image.load('Object Images/restart.png'),
                   (250, 343), "Object Images/restart.png"), ]
        self.Active_buttons = [1, 1, 0]  # Pregame screen uses first 2 buttons

        self.Cat_buttons = [
            Button(pg.image.load('Cat Images/orangeright_80.png'),
                   (90, 310), "cat1"),
            Button(pg.image.load('Cat Images/greyright_80.png'),
                   (250, 310), "cat2"),
            Button(pg.image.load('Cat Images/blueright_80.png'),
                   (410, 310), "cat3"), ]
        self.Chosen_cat = ""

        # Initialize background for different game state screens.
        self.background = pg.image.load('Background Images/purplebg.png')
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        self.start_background = pg.image.load(
            'Background Images/startscreen.png')
        self.choose_cat_background = pg.image.load(
            'Background Images/pickcat1.png')
        self.end_background = pg.image.load('Background Images/endscreen.png')
        self.start_background = pg.transform.scale(
            self.start_background, (WIDTH, HEIGHT))
        self.choose_cat_background = pg.transform.scale(
            self.choose_cat_background, (WIDTH, HEIGHT))
        self.end_background = pg.transform.scale(
            self.end_background, (WIDTH, HEIGHT))

        self._width = WIDTH
        self._height = HEIGHT
        self.score = 0          # Initialize player's score
        self.lives = 9          # Initialize player's lives
        self.game_state = 0     # Initialize game state to pregame
        self.cycles = 0         # Used for animation
        self.map = []
        self.h_spacing = 10     # Set vertical spacing between platforms
        self.myfont = pg.font.Font('slkscr.ttf', 50)

        # Initialize empty lists in which we store instances of different game
        # components.
        self.Players = self.ReferenceLadders = []
        self.Fireballs = self.Stars = self.Platforms = []
        self.Ladders = self.ReferencePlatforms = []
        self.ReferenceEndcaps = []
        self.ReferenceCats = []

        # Initialize pygame sprite groups
        # which we use to display instances on screen.
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.star_group = pg.sprite.RenderPlain(self.Stars)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.ref_platform_group = pg.sprite.RenderPlain(self.ReferencePlatforms)
        self.ref_ladder_group = pg.sprite.RenderPlain(self.ReferenceLadders)
        self.ref_endcap_group = pg.sprite.RenderPlain(self.ReferenceEndcaps)
        self.ref_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)

        # Resets the above groups and initializes the game
        self.reset_groups(0, 9)

    def reset_groups(self, score, lives):
        """
        Reset game components. This includes the score, lives, map,
        and lists of game component instances.

        Args:
            score: An int that represents player's current score.
            lives: An int that represents player's current number of lives.
        """
        self.score = score
        self.lives = lives
        self.map = []
        self.Players = Player(pg.image.load('Cat Images/orangefront.png'),
                              (self._width // 2, self._height - 25))
        self.Stars = []
        self.Platforms = []
        self.Fireballs = []
        self.Ladders = []
        self.ReferencePlatforms = []
        self.ReferenceLadders = []
        self.ReferenceEndcaps = []
        self.ReferenceCats = ReferenceCat(pg.image.load(
            'Object Images/reference.png'),
            (self._width // 2, self._height - 35))
        self.initialize_game()  # Initialize game and generate map
        self.create_groups()    # Create instance groups

    def initialize_game(self):
        """
        Initialize the game by calling the methods to make the map, generate
        platforms, ladders, and stars randomly, populating the map with our
        game components, then creating the groups of those game components.
        """
        # Loop to keep generating board components until we get one
        # where player has a path to the top
        while True:
            self.map = []
            self.make_map()
            self.Ladders = self.Platforms = []
            self.ReferenceEndcaps = []
            self.generate_platforms()
            self.generate_ladders()
            if self.is_top_reachable(25, 0) is True:
                break
        self.make_boundaries()
        self.create_ladder_reference()
        self.create_reference_lines()
        self.create_endcap_reference_lines()
        self.generate_stars()
        self.create_groups()

    def create_groups(self):
        """
        Render the game compone nts as PyGame Sprites.
        """
        self.ref_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)
        self.platform_group = pg.sprite.RenderPlain(self.Platforms)
        self.star_group = pg.sprite.RenderPlain(self.Stars)
        self.ladder_group = pg.sprite.RenderPlain(self.Ladders)
        self.fireball_group = pg.sprite.RenderPlain(self.Fireballs)
        self.ref_ladder_group = pg.sprite.RenderPlain(self.ReferenceLadders)
        self.ref_platform_group = pg.sprite.RenderPlain(self.ReferencePlatforms)
        self.ref_endcap_group = pg.sprite.RenderPlain(self.ReferenceEndcaps)
        self.player_group = pg.sprite.RenderPlain(self.Players)
        self.ref_cat_group = pg.sprite.RenderPlain(self.ReferenceCats)

    def make_map(self):
        """
        Create an empty map.
        """
        # Make 2D array filled with zeros
        for _ in range(0, self._height // 10 + 1):
            row = []
            for _ in range(0, self._width // 10 + 1):
                row.append(0)
            self.map.append(row)

    def create_fireball(self, width):
        """
        Randomly generate fireballs.
        Generates fireballs on the screen such that
        there are no more than 3 at anytime on the screen
        """
        # Making it so the number of fireballs on the board cannot exceed 3 at
        # anytime.
        if len(self.Fireballs) < 3:
            # Initializing the x randomly between the length of the width
            # and the y position at a random point above the
            # board so that the fireballs don't all fall at the same
            # time
            location = (random.randint(5, width), random.randint(-1000, 0))
            # Add the fireball to the list
            self.Fireballs.append(Fireball(pg.image.load(
                'Object Images/fireball.png'),
                location, len(self.Fireballs), -3))
            self.create_groups()

    def fireball_check(self):
        """
        Update all the fireball positions and check for collisions with player.
        Makes the fireball fall down on the screen and if it collides
        with the player, then the player loses a life and the fireball
        disapears.
        """
        # Checking to see if the fireball collides with
        # the player
        for fireball in self.fireball_group:
            # Update the position of the fireball
            fireball.continuous_update(self.player_group)
            # If the fireball collides, then reduce a life
            if fireball.check_collision(self.player_group):
                self.Fireballs.remove(fireball)
                self.lives -= 1
                self.create_groups()
            # If the player loses a life, then change the gamestate
            # such that the game over screen is displayed
            if self.lives == 0:
                self.game_state = 3
                self.Active_buttons[0] = 0
                self.Active_buttons[1] = 0
                self.Active_buttons[2] = 1
            # If the fireball reaches the bottom of the screen, then
            # get rid of it
            if fireball.get_position()[1] >= 490:
                self.Fireballs.remove(fireball)

    def generate_stars(self):
        """
        Randomly generate stars (where there is a platform below the star so
        the player can reach it). Add the star to map and update star list.
        """
        width = len(self.map)
        height = len(self.map[0])
        w_spacing = 5  # Horizontal spacing between the stars
        offset = -8    # Vertical offset that places the star above the platform

        # Traverse the platforms
        for y in range(self.h_spacing, height, self.h_spacing):
            for x in range(w_spacing, width, w_spacing):
                rand_star = random.randint(1, 5)
                # Conditions to generate star:
                # If there is a platform on this level
                # 1/5 chance of a ladder being placed (for randomness)
                # If there isn't already a star to the left or right
                if self.map[x][y] == 1 and rand_star == 1 and \
                   self.map[x - w_spacing][y - 1] != 3 and \
                   self.map[x + w_spacing][y - 1] != 3:
                    self.map[x][y - 1] = 3
                    self.Stars.append(Star(pg.image.load(
                        'Object Images/yellow star.png'),
                        (x * 10, (y - 1) * 10 + offset)))
        # If less than 3 stars are generated, call the function again
        if len(self.Stars) < 3:
            self.generate_stars()

    def make_boundaries(self):
        """
        Add boundaries to the left and right sides of our map.
        """
        height = len(self.map)
        width = len(self.map[0])
        for j in range(0, height):
            self.map[0][j] = 4
            self.map[width - 1][j] = 4

    def generate_platforms(self):
        """
        Randomly generate platforms.
        Add the platform to map and update platforms list.
        """
        height = len(self.map)
        width = len(self.map[0])

        # Generate platforms at all levels except for ground
        for y in range(0, height - self.h_spacing, self.h_spacing):
            x = 1
            while x < width:
                rand_platform_size = random.randint(7, 15)
                for i in range(rand_platform_size):
                    self.map[x][y] = 1
                    self.Platforms.append(Platform(
                        pg.image.load('Object Images/platform28.png'),
                        (x * 10 + 5, y * 10 + 5)))
                    x += 1
                    if x >= width - 1:
                        break
                rand_space = random.randint(7, 15)
                if random.randint(0, 1) == 0:
                    x += rand_space

        # Create ground floor
        for i in range(0, width):
            self.map[i][height - 1] = 1
            self.Platforms.append(Platform(
                pg.image.load('Object Images/platform28.png'),
                (i * 10 + 10 / 2, (height - 1) * 10 + 10 / 2)))

    def generate_ladders(self):
        """
        Randomly generate ladders between two platforms.
        Add the ladder to map and update ladders list.
        """
        height = len(self.map) - 1
        width = len(self.map[0]) - 1
        w_spacing = 6    # Horizontal spacing between the ladders

        # Loop through each platform level
        for y in range(0, height, self.h_spacing):
            num_on_this_lvl = 0
            # Randomly decide if there should be 1 platform on this level or 2
            rand_num = random.randint(1, 2)
            while num_on_this_lvl < rand_num:
                for x in range(w_spacing, width - w_spacing, w_spacing):
                    rand_ladder = random.randint(1, 7)
                    if num_on_this_lvl == rand_num:
                        break
                    # Conditions to generate ladder:
                    # If there is a platform on this level and one level lower
                    # 1/7 chance of a ladder being placed (for randomness)
                    # If there isn't already a ladder to the left or right
                    elif self.map[x][y] == 1 \
                        and self.map[x][y + self.h_spacing] == 1 \
                        and rand_ladder == 1 \
                        and self.map[x - w_spacing][y] != 2 and \
                            self.map[x + w_spacing][y] != 2:
                        # Call helper method to create a ladder to connect
                        # between upper and lower platform
                        self.create_ladder(x, y, y + self.h_spacing)
                        num_on_this_lvl += 1

    def create_ladder(self, x, upper_y, lower_y):
        """
        Helper method to create a ladder between two platforms.

        Args:
            upper_y: y position of the upper platfrom.
            lower_y: y position of the lower platfrom.
        """
        # Given an upper and lower platform, connect them with ladder objects
        # with a vertical spacing of 3
        for y in range(upper_y, lower_y - 1, 3):
            self.map[x][y] = 2
            self.Ladders.append(Ladder(pg.image.load(
                                'Object Images/ladder figure.png'),
                               (x * 10 + 5, y * 10 + 10)))
        # Manually set the map value right above the lower platform
        # to be a ladder value, as the loop doesn't reach here
        self.map[x][lower_y - 1] = 2
        # For visual purposes, have a ladder image above the upper platform
        self.Ladders.append(Ladder(pg.image.load(
                            'Object Images/ladder figure.png'),
                           (x * 10 + 5, (upper_y - 1) * 10 + 10)))

    def is_top_reachable(self, x, y):
        """
        Recursive method to check that player has a path to reach the top.

        Args:
            x: x position of starting point.
            y: y position of starting point.
        """
        height = len(self.map)
        # Base case: If reached the other end of the board
        if y == height - 1:
            return True
        # Find position of next possible ladder to use
        next_ladder = self.traverse_left_right(x, y)
        # If the value of the ladder to the left is valid,
        # call the function again
        if next_ladder[0] != 0 and self.map[next_ladder[0]][y] == 2:
            return self.is_top_reachable(next_ladder[0], y + self.h_spacing)
        # If the value of the ladder to the right is valid,
        # call the function again
        if next_ladder[1] != 49 and self.map[next_ladder[1]][y] == 2:
            return self.is_top_reachable(next_ladder[1], y + self.h_spacing)
        else:
            return False

    def traverse_left_right(self, x, y):
        """
        Helper method to find ladders to the left and right of given position.

        Args:
            x: x position of starting point.
            y: y position of platform that we are traversing.
        """
        left = right = x
        # Keep updating left value until we reach the left edge of the
        # board or we encounter a platform gap
        while left > 0:
            if self.map[left][y] == 2 or (y > 0 and self.map[left][y] == 0):
                break
            left -= 1
        height = len(self.map)
        # Keep updating right value until we reach the right edge of the
        # board or we encounter a platform gap
        while right < height - 2:
            if self.map[right][y] == 2 or (y > 0 and self.map[right][y] == 0):
                break
            right += 1
        return (left, right)

    def create_reference_lines(self):
        """
       Create reference lines for the platforms.
       Reference lines are created along the top edge of the platform
       to help define the movement of the player. If the player
       is colliding with these lines then it can move left and
       right.
        """
        # loading the image used as a reference for the platform
        ref_image = 'Object Images/reference.png'
        # Traversing across the map
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                # Checking to find a platform which is indexed as 1
                if self.map[j][i] == 1:
                    self.ReferencePlatforms.append(ReferencePlatform(
                        pg.image.load(ref_image), (j * 10, (i - 2) * 10 + 8)))
                    self.ReferencePlatforms.append(ReferencePlatform(
                        pg.image.load(ref_image), (j * 10, (i - 3) * 10 + 8)))
                    # If the index is not at the end of the map
                    if j != len(self.map) - 1:
                        # If it is a platform edge then add two reference
                        # at the end so that the player wont get stuck
                        # at the edge of the platform
                        if self.map[j + 1][i] == 0 or self.map[j + 1][i] == 4:
                            self.ReferencePlatforms.append(ReferencePlatform(
                                pg.image.load(ref_image),
                                ((j + 1) * 10, (i - 2) * 10 + 8)))
                            self.ReferencePlatforms.append(ReferencePlatform(
                                pg.image.load(ref_image),
                                ((j + 2) * 10, (i - 2) * 10 + 8)))
                        if self.map[j - 1][i] == 0 or self.map[j - 1][i] == 4:
                            self.ReferencePlatforms.append(ReferencePlatform(
                                pg.image.load(ref_image),
                                ((j - 1) * 10, (i - 2) * 10 + 8)))
                            self.ReferencePlatforms.append(ReferencePlatform(
                                pg.image.load(ref_image),
                                ((j - 2) * 10, (i - 2) * 10 + 8)))

    def create_ladder_reference(self):
        """
       Create reference lines for the ladders.
       Reference lines are created along the length of the ladder
       to help define the movement of the player. If the player
       is colliding with these lines then it can move up and down.
        """
        # Loading the image used a reference for the ladders
        ref_ladder_image = 'Object Images/referenceladder.png'
        # Traverse across the map
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                # Checking to find a platform which is indexed as 2
                # and a ladder reference point at a certain position close
                # to that line
                if self.map[j][i - 1] == 2:
                    self.ReferenceLadders.append(ReferenceLadder(
                        pg.image.load(ref_ladder_image), (
                                     (j * 10) + 5,
                                     ((i + 2) * 10) - 34)))

    def create_endcap_reference_lines(self):
        """
       Create reference lines for the edges of the platforms.
       Reference lines are created along the edge of the platform
       to help define the movement of the player. If the player
       is colliding with these lines then it bounces from these
       lines.
        """
        # Loading the image used a reference for the ladders
        ref_ladder_image = 'Object Images/referenceladder.png'
        # Traversing across the map
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                # If a platform is found and the item at an index
                # next to the platform is empty indicating the end
                # of the platform then create an endcap reference
                if self.map[j][i] == 1:
                    if j != len(self.map) - 1:
                        # Checking to the right of the platform
                        if self.map[j + 1][i] == 0:
                            for k in range(i + 2, i + 6):
                                self.ReferenceEndcaps.append(ReferenceEndcap(
                                    pg.image.load(ref_ladder_image), (
                                                 (j + 2) * 10,
                                                 (k - 3) * 10 + 5)))
                        # Checking to left of platform
                        if self.map[j - 1][i] == 0:
                            for k in range(i + 2, i + 6):
                                self.ReferenceEndcaps.append(ReferenceEndcap(
                                    pg.image.load(ref_ladder_image), (
                                                 (j - 1) * 10,
                                                 (k - 3) * 10 + 5)))

    def star_check(self, stars_collected):
        """
        Perform star collection by updating score, star list, and map.
        This method is called if player has collided with a star.

        Args:
            stars_collected: A list of star instances that the player has
            collided with.
        """
        for star in stars_collected:
            self.score += 10         # Update score
            self.Stars.remove(star)  # Update list of Stars on screen
            self.create_groups()     # Update star group

    def process_button(self):
        """
        Perform needed actions when a button is clicked.
        """
        # If the start button is pressed
        if self.Active_buttons[0] == 1 and \
           self.Buttons[0].rect.collidepoint(pg.mouse.get_pos()):
            self.game_state = 1
            self.Active_buttons = [0, 0, 0]
        # If the exit button is pressed
        if self.Active_buttons[1] == 1 and \
           self.Buttons[1].rect.collidepoint(pg.mouse.get_pos()):
            pg.quit()
            sys.exit()
        # If the restart button is pressed
        if self.Active_buttons[2] == 1 and \
           self.Buttons[2].rect.collidepoint(pg.mouse.get_pos()):
            self.reset_groups(0, 9)
            self.game_state = 1

    def select_cat(self):
        """
        Process which cat the player has chosen based on which
        cat button is clicked on, then update game state.
        """
        if self.Cat_buttons[0].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "orange"
        if self.Cat_buttons[1].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "grey"
        if self.Cat_buttons[2].rect.collidepoint(pg.mouse.get_pos()):
            self.Chosen_cat = "blue"
        self.game_state = 2

    def check_button(self):
        """
        Check for mouse hovering over buttons to change their images
        giving a hover button effect.
        """
        mouse_pos = pg.mouse.get_pos()
        for button in range(len(self.Buttons)):
            # Active button
            if self.Active_buttons[button] == 1 and \
               self.Buttons[button].rect.collidepoint(mouse_pos):
                if button == 0:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/hov_start_meow.png'))
                elif button == 1:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/hov_exit_game.png'))
                elif button == 2:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/hov_restart.png'))
            # Inactive button
            else:
                if button == 0:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/start_meow.png'))
                elif button == 1:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/exit_game.png'))
                elif button == 2:
                    self.Buttons[button].change_image(
                        pg.image.load('Object Images/restart.png'))

        for button in range(len(self.Cat_buttons)):
            # Active button
            if self.Cat_buttons[button].rect.collidepoint(mouse_pos):
                if button == 0:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/orangefront_80.png'))
                elif button == 1:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/greyfront_80.png'))
                elif button == 2:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/bluefront_80.png'))
            # Inactive button
            else:
                if button == 0:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/orangeright_80.png'))
                elif button == 1:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/greyright_80.png'))
                elif button == 2:
                    self.Cat_buttons[button].change_image(
                        pg.image.load('Cat Images/blueright_80.png'))

    def redraw_screen(self, display_screen, score_label,
                      lives_label, width, height):
        """
        Redraws the entire game screen.

        Game states:
        0 Game lobby
        1 Choose cat
        2 Gameplay
        3 End screen

        Args:
            display_screen: PyGame display.
            score_label: rendering of the score.
            width: An integer representing the width of the screen.
            height: An integer representing the height of the screen.
        """
        # Fill display screen with black
        display_screen.fill((0, 0, 0))

        # If we are in either pregame or postgame states
        if self.game_state == 0 or self.game_state == 3:
            if self.game_state == 0:
                # Pre game state
                display_screen.blit(self.start_background,
                                    self.start_background.get_rect())
            if self.game_state == 3:
                # Post game state
                display_screen.blit(self.end_background,
                                    self.end_background.get_rect())
                label = self.myfont.render(str(self.score), 10, (255, 255, 255))
                display_screen.blit(label, (285, 255))

            # Display the active buttons
            for button in range(len(self.Active_buttons)):
                if self.Active_buttons[button] == 1:
                    display_screen.blit(self.Buttons[button].image,
                                        self.Buttons[button].get_top_left_pos())

        # If we are choosing a cat
        if self.game_state == 1:
            display_screen.blit(self.choose_cat_background,
                                self.choose_cat_background.get_rect())
            # Display the cat buttons
            for button in range(len(self.Cat_buttons)):
                display_screen.blit(self.Cat_buttons[button].image,
                                    self.Cat_buttons[button].get_top_left_pos())

        # If we are in the game state,
        if self.game_state == 2:
            # Draw the background first
            display_screen.blit(self.background, self.background.get_rect())
            # Draw all our groups on the background
            self.platform_group.draw(display_screen)
            self.ladder_group.draw(display_screen)
            self.star_group.draw(display_screen)
            self.player_group.draw(display_screen)
            self.fireball_group.draw(display_screen)
            # self.ref_cat_group.draw(display_screen)
            # self.ref_platform_group.draw(display_screen)
            # self.ref_ladder_group.draw(display_screen)
            # self.ref_endcap_group.draw(display_screen)

            # Display the player's score and lives in the lower
            # left and right corners of the screen.
            display_screen.blit(score_label, (15, 470))
            display_screen.blit(lives_label, (390, 470))

    def update_level(self, current_score, current_lives):
        """
        Initialize the game, preserving the player's score and
        remaining number of lives.

        Args:
            current_score: player's current score.
            current_lives: player's current number of lives.
        """
        self.reset_groups(current_score, current_lives)
