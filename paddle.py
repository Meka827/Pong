import pygame


class Paddle:
    """A class to manage the paddle"""

    def __init__(self, pong_game):
        """Initalize the paddle and set it's starting position."""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)


class P_Paddle(Paddle):
    """A class for the player paddle"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        # load the paddle image
        self.image = pygame.image.load("images/fancy-paddle-blue.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft


class O_Paddle(Paddle):
    """A class for the opponent paddle"""

    def __init__(self, pong_game):
        super().__init__(pong_game)
        # load the paddle image
        self.image = pygame.image.load("images/fancy-paddle-green.png")
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright
