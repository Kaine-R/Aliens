import random
import pygame
from pygame.sprite import Sprite
import time

class Ball(Sprite):
    def __init__(self, screen, settings, menu):
        super(Ball, self).__init__()
        self.size = 15
        self.rect = pygame.Rect(250, 250, self.size, self.size)
        self.screen = screen
        self.screenRect = screen.get_rect()

        if random.randint(0, 2) == 0:
            self.movingUp = False
        else:
            self.movingUp = True
        if random.randint(0,2) == 0:
            self.movingLeft = False
        else:
            self.movingLeft = True


        self.varience = random.randint(1, 4) / 10

        self.settings = settings
        self.rect.y = self.screenRect.bottom / 2
        self.rect.centerx = self.screenRect.centerx
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self, settings, gameStats, scores, balls):
        if self.movingUp:
            self.y -= settings.ballSpeed
            if self.y < 0:
                if self.x <= self.screenRect.right/2:
                    gameStats.playerScore += 1
                else:
                    gameStats.botScore += 1
                scores.prepScore(gameStats)
                time.sleep(0.5)
                balls.remove(self)
        else:
            self.y += settings.ballSpeed
            if self.y > self.screenRect.bottom - self.size:
                if self.x <= self.screenRect.right/2:
                    gameStats.playerScore += 1
                else:
                    gameStats.botScore += 1
                scores.prepScore(gameStats)
                time.sleep(0.5)
                balls.remove(self)


        if self.movingLeft:
            self.x -= settings.ballSpeed + self.varience / 2
            if self.x < -1:
                gameStats.playerScore += 1
                scores.prepScore(gameStats)
                time.sleep(0.5)
                balls.remove(self)
        else:
            self.x += settings.ballSpeed + self.varience / 2
            if self.x > self.settings.screenWidth - self.size:
                gameStats.botScore += 1
                scores.prepScore(gameStats)
                time.sleep(0.8)
                balls.remove(self)

        self.rect.x, self.rect.y = self.x, self.y

    def drawBall(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
