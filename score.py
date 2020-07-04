import pygame


class Score:
    def __init__(self, pong_game):
        pygame.font.init()
        """Initalize the scoreboard"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings
        self.score = 0
        self.scorefont = pygame.font.Font(None, 96)
        self.scoretext = self.scorefont.render(str(self.score), False, (255, 255, 255))
        self.rect = self.scoretext.get_rect()

    def blitme(self):
        """Draw the object at it's current location"""
        self.screen.blit(self.scoretext, self.rect)

    def update_score(self):
        self.score += 1
        self.scoretext = self.scorefont.render(str(self.score), False, (255, 255, 255))
        print(self.score)


class P_Score(Score):
    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.rect.topleft = self.screen_rect.topleft


class O_Score(Score):
    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.rect.topright = self.screen_rect.topright

