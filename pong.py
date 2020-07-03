import pygame
import sys

from settings import Settings
from screen_obj import screen_obj, P_Paddle, O_Paddle, Ball


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
        self.ball = Ball(self)
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self.ball.update()
            self._check_events()
            self.p_paddle.update()
            self.o_paddle.update()
            self._update_screen()
            self.clock.tick(self.settings.clock)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.o_paddle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.o_paddle.moving_down = True
        elif event.key == pygame.K_w:
            self.p_paddle.moving_up = True
        elif event.key == pygame.K_s:
            self.p_paddle.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.o_paddle.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.o_paddle.moving_down = False
        elif event.key == pygame.K_w:
            self.p_paddle.moving_up = False
        elif event.key == pygame.K_s:
            self.p_paddle.moving_down = False

    def collisions(self):
        if self.ball.rect.collidelist([self.o_paddle.rect, self.p_paddle.rect]) != -1:
            self.ball.bounce()
        if self.ball.rect.x >= 1200:
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.x <= 0:
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.y > 800:
            self.ball.velocity[1] = -self.ball.velocity[1]
        if self.ball.rect.y < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.p_paddle.blitme()
        self.o_paddle.blitme()
        self.ball.blitme()
        self.collisions()
        pygame.display.flip()


if __name__ == "__main__":
    pong = Pong()
    pong.run_game()
