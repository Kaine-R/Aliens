import pygame.font


class ScoreBoard():
    def __init__(self, screen, settings, gameStats):
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.width, self.height = 250, 50
        self.scoreColor = (40, 40, 40)
        self.textColor = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.screenRect.left
        self.rect2.x = self.screenRect.right - self.width - 10

        self.prepScore(gameStats)

    def prepScore(self, gameStats):
        self.msgImage = self.font.render("Bot Score: " + str(gameStats.botScore), True, self.textColor, self.scoreColor)
        self.imageRect = self.msgImage.get_rect()
        self.imageRect.center = self.rect.center

        self.msgImage2 = self.font.render("Player Score: " + str(gameStats.playerScore), True, self.textColor, self.scoreColor)
        self.imageRect2 = self.msgImage2.get_rect()
        self.imageRect2.center = self.rect2.center

    def showScore(self):
        self.screen.blit(self.msgImage, self.imageRect)
        self.screen.blit(self.msgImage2, self.imageRect2)


