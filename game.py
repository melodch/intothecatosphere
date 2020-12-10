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
        self.width = WIDTH
        self.height = HEIGHT
        self.display_screen = pg.display.set_mode((self.width, self.height))
        self.new_game = Board()
        self.player_group = self.new_game.player_group
        self.platform_group = self.new_game.platform_group
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
            self.score_label = self.myFont.render(str(self.new_game.score), 1,
                                                    (0, 0, 0))
            self.lives_label = self.myFont.render(str(self.new_game.lives), 1,
                                                    (0, 0, 0))
            # If the game state is not 1 then we will not have to run the game,
            # we just need to display buttons
            if self.new_game.gameState != 1:

                self.new_game.check_button()  # Checks the buttons for hover effects
                self.new_game.redraw_screen(self.display_screen, self.score_label,self.lives_label, self.width,
                                          self.height)  # Redraws the buttons onto the screen

                for event in pg.event.get():
                    # Exit to desktop
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEBUTTONUP:
                        # Check which button was clicked and change game state accordingly
                        self.new_game.process_button()  
                        # Assign groups again
                        self.player_group = self.new_game.player_group
                        self.platform_group = self.new_game.platform_group
                        self.ladder_group = self.new_game.ladder_group

            # If game state is 1 then run the game:
            if self.new_game.gameState == 1:
                self.gem_group = self.new_game.gem_group

                # Get the appropriate groups
                # Create fireballs
                self.new_game.create_fireball(self.width)
                # Check for collisions below
                # Check for collisions above
                #self.new_game.Players[0].updateY(-2)
                self.wallsCollidedAbove = self.new_game.Players.check_collision(self.platform_group)
                #self.new_game.Players[0].updateY(2)
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
                #self.new_game.Players[0].continuousUpdate(self.platform_group, self.ladder_group)
                keys = pg.key.get_pressed()
                #Change this
                if keys[K_RIGHT]:
                    ladders_collided = self.new_game.Players.check_collision(self.ladder_group)

                    #collisions down
                    self.new_game.Players.update_position(pg.image.load('player.png'), -2,'V')                    
                    walls_collided_down = self.new_game.Players.check_collision(self.platform_group)
                    self.new_game.Players.update_position(pg.image.load('player.png'), 2,'V') 
                    
                    #collisions up
                    self.new_game.Players.update_position(pg.image.load('player.png'), 2,'V')
                    walls_collided_up = self.new_game.Players.check_collision(self.platform_group)
                    self.new_game.Players.update_position(pg.image.load('player.png'), -2,'V') 
                    
                    # moving character
                    if (walls_collided_down != []) and (walls_collided_up == []):                        
                        self.new_game.Players.update_position(pg.image.load('player.png'), -self.new_game.Players.get_speed(), 'H')
                    
                    # if ladders_collided == [] and walls_collided_up == [] and walls_collided_down:
                    #     self.new_game.Players.update_position(pg.image.load('player.png'), -self.new_game.Players.get_speed(), 'V')

                if keys[K_LEFT]:
                    ladders_collided = self.new_game.Players.check_collision(self.ladder_group)
                    #collisions down
                    self.new_game.Players.update_position(pg.image.load('player.png'), -2,'V')                    
                    walls_collided_down = self.new_game.Players.check_collision(self.platform_group)
                    self.new_game.Players.update_position(pg.image.load('player.png'), 2,'V') 
                    
                    #collisions up
                    self.new_game.Players.update_position(pg.image.load('player.png'), 2,'V')
                    walls_collided_up = self.new_game.Players.check_collision(self.platform_group)
                    self.new_game.Players.update_position(pg.image.load('player.png'), -2,'V') 
                    
                    #moving character
                    if (walls_collided_down != []) and (walls_collided_up == []):                        
                        self.new_game.Players.update_position(pg.image.load('player.png'), self.new_game.Players.get_speed(), 'H')

                    # if ladders_collided == [] and walls_collided_up == [] and walls_collided_down == []:
                    #     self.new_game.Players.update_position(pg.image.load('player.png'), -self.new_game.Players.get_speed(), 'V')

                if keys[K_DOWN]:
                    walls_collided = self.new_game.Players.check_collision(self.platform_group)
                    ladders_collided = self.new_game.Players.check_collision(self.ladder_group)
                    if ladders_collided:
                        self.new_game.Players.update_position(pg.image.load('player.png'), -self.new_game.Players.get_speed(),'V')
                    if ladders_collided == [] and walls_collided_up == [] and walls_collided_down == []:
                        self.new_game.Players.update_position(pg.image.load('player.png'), -self.new_game.Players.get_speed(), 'V')

                if keys[K_UP]:
                    ladders_collided = self.new_game.Players.check_collision(self.ladder_group)
                    if ladders_collided:
                        self.new_game.Players.update_position(pg.image.load('player.png'), self.new_game.Players.get_speed(),'V')
  
                
               

                # Redraw all instances onto the screen
                self.new_game.redraw_screen(self.display_screen,
                                            self.score_label,self.lives_label,
                                            self.width, self.height)

                # Update the fireball and check for collisions with player.
                self.new_game.fireball_check()

                # Check for gem collection
                gems_collected = pg.sprite.spritecollide(self.new_game.Players,
                                                         self.gem_group, True)
                self.new_game.gem_check(gems_collected)

                # Update the display to view changes
            pg.display.update()
