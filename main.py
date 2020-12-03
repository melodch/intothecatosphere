import pygame as pg
from game import Game


# Main loop for playing the game
if __name__ == "__main__":
    pg.init()
    # Instantiate the Game class and run the game
    createdGame = Game()
    createdGame.runGame()
