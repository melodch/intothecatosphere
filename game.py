import pygame as pg
import sys
from board import Board
from constants import *


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
        self.width = constants.width
        self.height = constants.height
        self.displayScreen = pg.display.set_mode((self.width, self.height))
        self.newGame = Board(self.width, self.height)
        self.player_group = self.newGame.player_group
        self.platform_group = self.newGame.platform_group

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

        # If game state is 1 then run the game:
        if self.newGame.gameState == 1:
            self.gem_group = self.newGame.gem_group
            
        # Get the appropriate groups
        # Create fireballs
        # Check for collisions below
        # Check for collisions above
        self.newGame.Players[0].updateY(-2)
        self.wallsCollidedAbove = self.newGame.Players[0].checkCollision(self.wall_group)
        self.newGame.Players[0].updateY(2)
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
        self.newGame.Players[0].continuousUpdate(self.platform_group, self.ladder_group)
        #Change this
        if keyState[pg.K_d]:

            # Check which key is being pressed, update position accordingly
            self.newGame.Players[0].update_position(pg.image.load('Assets/right.png'), self.newGame.Players[0].getSpeed(), 'H')
            # If we have collided a wall, move the player back to where he was in the last state
            platforms_collided = self.newGame.Players[0].checkCollision(self.platform_group)
            if platforms_collided: 
                self.newGame.Players[0].update_position(pg.image.load('Assets/left.png'), -self.newGame.Players[0].getSpeed(), 'H')

        if keyState[pg.K_a]:

            # Check which key is being pressed, update position accordingly
            self.newGame.Players[0].update_position(pg.image.load('Assets/right.png'), -self.newGame.Players[0].getSpeed(), 'H')
            # If we have collided a wall, move the player back to where he was in the last state
            wallsCollided = self.newGame.Players[0].checkCollision(self.platform_group)
            if wallsCollided: 
                self.newGame.Players[0].update_position(pg.image.load('Assets/left.png'), self.newGame.Players[0].getSpeed(),'H')
        
        if keyState[pg.K_s]:
            self.newGame.Players[0].update_position(pg.image.load('Assets/still.png'), -10, 'V')
            wallsCollided = self.newGame.Players[0].checkCollision(self.platform_group)
            if wallsCollided: 
                self.newGame.Players[0].update_position(pg.image.load('Assets/left.png'), 10,'V')

        
        # Redraw all instances onto the screen
        self.newGame.redrawScreen(self.displayScreen, self.scoreLabel, self.width, self.height)

        # Update the fireball and check for collisions with player.
        
        # Check for gem collection
        gems_collected = pg.sprite.spritecollide(self.newGame.Players[0], self.gem_group, True)
        self.newGame.gem_check(gems_collected)

        # Update the display to view changes
        pygame.display.update()
