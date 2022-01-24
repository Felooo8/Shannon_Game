"""
This file runs the app.
"""

from the_game.game import Game


def main():
    """
    Starts the game.
    """
    game = Game()
    game.start()
    game.play()


if __name__ == "__main__":
    main()
