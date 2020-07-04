import pygame


class Text_Obj:
    def __init__(self, pong_game):
        pygame.font.init()
        """Initalize the textobjboard"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings
        self.textobj = 0
        self.textobjfont = pygame.font.Font(None, 96)
        self.textobjtext = self.textobjfont.render(
            str(self.textobj), False, (255, 255, 255)
        )
        self.rect = self.textobjtext.get_rect()

    def blitme(self):
        """Draw the object at it's current location"""
        self.screen.blit(self.textobjtext, self.rect)

    def update_textobj(self):
        self.textobj += 1
        self.textobjtext = self.textobjfont.render(
            str(self.textobj), False, (255, 255, 255)
        )


class P_Score(Text_Obj):
    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.rect.topleft = self.screen_rect.topleft


class O_Score(Text_Obj):
    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.rect.topright = self.screen_rect.topright


class Victory_text(Text_Obj):
    def __init__(self, pong_game, winner):
        super().__init__(pong_game)
        self.winner = winner
        self.textobj = self.winner
        self.textobjfont = pygame.font.Font(None, 45)
        self.textobjtext = self.textobjfont.render(
            str(self.textobj), False, (255, 255, 255)
        )
        self.rect.center = self.screen_rect.center

    def update_textobj(self):
        self.textobj = ""
        self.textobjtext = self.textobjfont.render(
            str(self.textobj), False, (255, 255, 255)
        )
