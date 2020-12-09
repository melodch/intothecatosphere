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
        display_screen: PyGame display to view the game
        new_game: new instance of the Board class
        fireball_timer: timer that controls how fast fireballs are generated
        gem_group: group from the Board instance that represent
        gem instances on the screen
        platform_group: group from the Board instance that represent
        platform instances on the screen
        ladder_group: group from the Board instance that represent
        ladder instances on the screen
    """

    def __init__(self):
        """
        Set up a game that creates a new Board instance and assigns groups
        from this instance to the group attributes. Initialize the rest of the
        instance attributes.
        """
        self.width = width
        self.height = height
        self.display_screen = pg.display.set_mode((self.width, self.height))
        self.newGame = Board()
        self.player_group = self.newGame.player_group
        self.platform_group = self.newGame.platform_group
        # constants
        self.FPS = 100
        self.clock = pg.time.Clock()
        self.myFont = pg.font.SysFont("comicsansms", 30)

    def runGame(self):
        """
        Run the main loop that displays the board, gets user input,
        and makes changes to the board.

        Since our game goes on infinitely, we have the code that runs the game
        in a while loop that exits only when the player dies.
        """
        # Display the score on the screen

        # If game state is not 1 then don't run the game,
        # just display menu buttons
        # Check which button was clicked and change game state accordingly
        while True:

            self.clock.tick(self.FPS)
            self.score_label = self.myFont.render(str(self.newGame.score), 1,
                                                    (0, 0, 0)) 
            # If the game state is not 1 then we will not have to run the game, we just need to display buttons
            if self.newGame.gameState != 1:

                self.newGame.redraw_screen(self.display_screen, self.score_label, self.width,
                                          self.height)  # Redraws the buttons onto the screen

                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEBUTTONUP:
                        self.newGame.process_button()  # Check which button was clicked and change game state accordingly
                        # Assign groups again
                        self.player_group = self.newGame.player_group
                        self.platform_group = self.newGame.platform_group
                        # self.ladderGroup = self.newGame.ladderGroup
        
            # If game state is 1 then run the game:
            if self.newGame.gameState == 1:
                self.gem_group = self.newGame.gem_group
                
                # Get the appropriate groups
                # Create fireballs
                self.newGame.create_fireball(self.width, 0)
                # Check for collisions below
                # Check for collisions above
                #self.newGame.Players[0].updateY(-2)
                self.wallsCollidedAbove = self.newGame.Players.check_collision(self.platform_group)
                #self.newGame.Players[0].updateY(2)
                # Set the on_ladder state of the player

                # In a PyGame event loop, check which key is being pressed:
                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                # If QUIT, exit to desktop

                # If KEYDOWN,
                # If quit key pressed:
                # We quit the game and go to the restart screen

                # If up key pressed and player is on a ladder:
                # Set the player to move up

                # Update the player's position
                #self.newGame.Players[0].continuousUpdate(self.platform_group, self.ladder_group)
                keys = pg.key.get_pressed()
                #Change this
                if keys[K_RIGHT]:

                    # Check which key is being pressed, update position accordingly
                    self.newGame.Players.update_position(pg.image.load('player.png'), self.newGame.Players.get_speed(), 'H')
                    # If we have collided a wall, move the player back to where he was in the last state
                    platforms_collided = self.newGame.Players.check_collision(self.platform_group)
                    if platforms_collided: 
                        self.newGame.Players.update_position(pg.image.load('player.png'), -self.newGame.Players.get_speed(), 'H')

                if keys[K_LEFT]:

                    # Check which key is being pressed, update position accordingly
                    self.newGame.Players.update_position(pg.image.load('player.png'), -self.newGame.Players.get_speed(), 'H')
                    # If we have collided a wall, move the player back to where he was in the last state
                    wallsCollided = self.newGame.Players.check_collision(self.platform_group)
                    if wallsCollided: 
                        self.newGame.Players.update_position(pg.image.load('player.png'), self.newGame.Players.get_speed(),'H')
                
                if keys[K_DOWN]:
                    self.newGame.Players.update_position(pg.image.load('player.png'), 10, 'V')
                    wallsCollided = self.newGame.Players.check_collision(self.platform_group)
                    if wallsCollided: 
                        self.newGame.Players.update_position(pg.image.load('player.png'), -10,'V')

                # if keys[K_UP]:                  
                #     laddersCollided = self.newGame.Players.check_collision(self.ladder_group)
                #     if laddersCollided: 
                #         self.newGame.Players.update_position(pg.image.load('player.png'), self.newGame.Players.get_speed(),'V')

                

                # Redraw all instances onto the screen
                self.newGame.redraw_screen(self.display_screen, self.score_label, self.width, self.height)

                # Update the fireball and check for collisions with player.
                
                # Check for gem collection
                gems_collected = pg.sprite.spritecollide(self.newGame.Players, self.gem_group, True)
                self.newGame.gem_check(gems_collected)

                # Update the display to view changes
            pg.display.update()
