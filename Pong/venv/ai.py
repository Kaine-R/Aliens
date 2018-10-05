import pygame
from ball import Ball

class AI():
    def __init__(self, screen, settings, menu):
        self.width = 12
        self.height = 60
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, self.height, self.width)
        self.rect3 = pygame.Rect(0, 0, self.height, self.width)

        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings

        self.closeBall = Ball(screen, settings, menu)
        self.closeBall.x = self.screenRect.right

        self.rect.centerx = self.screenRect.left + 50
        self.rect.y = self.screenRect.bottom / 2
        self.y = float(self.rect.y)
        self.rect2.x, self.rect3.x = self.screenRect.right/4, self.screenRect.right/4
        self.rect2.y, self.rect3.y = 50, self.screenRect.bottom - 50
        self.x = float(self.rect2.x)

    def update(self, balls):
        for ball in balls:
            if ball.x < self.closeBall.x:
                self.closeBall = ball

        if self.closeBall.x < self.screenRect.right / 2:
            if self.y + self.height/5 > self.closeBall.y:
                self.y -= self.settings.AISpeed + .3
            elif self.y + self.height/2 < self.closeBall.y + self.height:
                self.y += self.settings.AISpeed + .3
        self.rect.y = self.y

        if self.x + self.height/5 < self.closeBall.x and self.x < self.screenRect.right/2 - self.height:
                self.x += self.settings.AISpeed + .3
        elif self.x + self.height/2 > self.closeBall.x and self.x > 0:
                self.x -= self.settings.AISpeed + .3
        self.rect2.x, self.rect3.x = self.x, self.x

    def drawAI(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect3)

    def reset(self):
        self.y = self.screenRect.bottom/2
        self.rect.y = self.y
        self.closeBall.x = self.screenRect.right