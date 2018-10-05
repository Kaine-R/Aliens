import pygame

class Player():
    def __init__(self, screen, settings):
        self.width = 12
        self.height = 60
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        self.rect.centerx = self.screenRect.right - 50
        self.rect.y = self.screenRect.bottom / 2
        self.y = float(self.rect.y)

        self.x = 3 * self.screenRect.width/4
        self.rect2 = pygame.Rect(0, 0, self.height, self.width)
        self.rect2.y = self.screenRect.top + 50
        self.rect3 = pygame.Rect(0, 0, self.height, self.width)
        self.rect2.x, self.rect3.x = self.x, self.x
        self.rect3.y = self.screenRect.bottom - 50

    def update(self):
        if self.movingUp and self.y > self.screenRect.top + 5:
            self.y -= self.settings.playerSpeed
        elif self.movingDown and self.y < self.screenRect.bottom - self.height - 5:
            self.y += self.settings.playerSpeed
        self.rect.y = self.y

        if self.movingLeft and self.x > self.screenRect.width / 2:
            self.x -= self.settings.playerSpeed
        elif self.movingRight and self.x < self.screenRect.right - self.rect.height - 5:
            self.x += self.settings.playerSpeed
        self.rect2.x, self.rect3.x = self.x, self.x

    def drawPlayer(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect3)

    def reset(self):
        self.y = self.screenRect.bottom/2
        self.rect.y = self.y
        self.x2 = self.screenRect.width / 2
        self.rect2.x, self.rect3.x = self.x, self.x

