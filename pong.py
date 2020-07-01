import pygame
import sys

from settings import Settings
from paddle import Paddle, P_Paddle, O_Paddle


class Pong:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Pong")
        self.p_paddle = P_Paddle(self)
        self.o_paddle = O_Paddle(self)

    def run_game(self):
        while True:
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.p_paddle.blitme()
        self.o_paddle.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    pong = Pong()
    pong.run_game()
