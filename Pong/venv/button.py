import pygame.font


class Button():
    def __init__(self, screen, settings, msg):
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.width, self.height = 250, 50
        self.buttonColor = (30, 100, 30)
        self.textColor = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        self.prepMsg(msg)

    def prepMsg(self, msg):
        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.imageRect = self.msgImage.get_rect()
        self.imageRect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.imageRect)