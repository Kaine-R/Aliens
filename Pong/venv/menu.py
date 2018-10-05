import pygame.font

class Menu:
    def __init__(self):
        self.difficulty = 0
        self.bgColor = (40, 40, 40)
        self.selectColor = (20, 100, 20)
        self.nonSelectColor = (90, 90, 90)
        self.font = pygame.font.SysFont(None, 40)
        self.first = True

    def prepMenu(self, screen, settings, balls, bot):
        setSize = (0, 0, 250, 100)
        self.screen = screen
        self.diffRect = pygame.Rect(setSize)
        self.diffOpt1Rect = pygame.Rect(setSize)
        self.diffOpt2Rect = pygame.Rect(setSize)
        self.diffOpt3Rect = pygame.Rect(setSize)
        self.pointRect = pygame.Rect(setSize)
        self.winnerRect = pygame.Rect(setSize)

        self.diffRect.y, self.pointRect.y = 7 * settings.screenHeight / 10, 8 * settings.screenHeight / 10
        self.diffRect.x, self.pointRect.x = settings.screenWidth/5, settings.screenWidth/4
        self.winnerRect.x, self.winnerRect.y = settings.screenWidth/2, settings.screenHeight/3

        self.pointImage = self.font.render("Score Limit: " + str(settings.scoreLimit), True, self.selectColor)
        self.pointImageRect = self.pointImage.get_rect()
        self.pointImageRect = self.pointRect


        self.pointMoreImage = self.font.render("More", True, self.selectColor)
        self.pointLessImage = self.font.render("Less", True, self.selectColor)
        self.pointMoreImageRect = self.pointMoreImage.get_rect()
        self.pointLessImageRect = self.pointLessImage.get_rect()
        self.pointMoreImageRect.x, self.pointMoreImageRect.y = 2 * settings.screenWidth/4, 8 * settings.screenHeight / 10
        self.pointLessImageRect.x, self.pointLessImageRect.y = 3 * settings.screenWidth/4, 8 * settings.screenHeight / 10

        self.diffImage = self.font.render("Difficulty level: ", True, self.selectColor)
        self.diffImageRect = self.diffImage.get_rect()
        self.diffImageRect.y = self.diffRect.y
        self.diffImageRect.x = self.diffRect.x
        if self.difficulty == 0:
            self.diffOpt1Image = self.font.render("Easy", True, self.selectColor)
        else:
            self.diffOpt1Image = self.font.render("Easy", True, self.nonSelectColor)
        if self.difficulty == 1:
            self.diffOpt2Image = self.font.render("Med", True, self.selectColor)
        else:
            self.diffOpt2Image = self.font.render("Med", True, self.nonSelectColor)
        if self.difficulty == 2:
            self.diffOpt3Image = self.font.render("Hard", True, self.selectColor)
        else:
            self.diffOpt3Image = self.font.render("Hard", True, self.nonSelectColor)

        self.diffOpt1ImageRect = self.diffOpt1Image.get_rect()
        self.diffOpt2ImageRect = self.diffOpt1Image.get_rect()
        self.diffOpt3ImageRect = self.diffOpt1Image.get_rect()

        self.diffOpt1ImageRect.x, self.diffOpt1ImageRect.y = 2 * settings.screenWidth/5, 7 * settings.screenHeight / 10
        self.diffOpt2ImageRect.x, self.diffOpt2ImageRect.y = 3 * settings.screenWidth/5, 7 * settings.screenHeight / 10
        self.diffOpt3ImageRect.x, self.diffOpt3ImageRect.y = 4 * settings.screenWidth/5, 7 * settings.screenHeight / 10


    def drawMenu(self):
        self.screen.blit(self.diffImage, self.diffImageRect)
        self.screen.blit(self.diffOpt1Image, self.diffOpt1ImageRect)
        self.screen.blit(self.diffOpt2Image, self.diffOpt2ImageRect)
        self.screen.blit(self.diffOpt3Image, self.diffOpt3ImageRect)
        self.screen.blit(self.pointImage, self.pointImageRect)
        self.screen.blit(self.pointMoreImage, self.pointMoreImageRect)
        self.screen.blit(self.pointLessImage, self.pointLessImageRect)


    def drawWin(self, gameStats, settings):
        if self.first == False:
            if gameStats.playerScore > gameStats.botScore:
                self.winnerImage = self.font.render("Player is the winner", True, self.selectColor)
            else:
                self.winnerImage = self.font.render("Bot is Winner", True, self.selectColor)
            self.winnerImageRect = self.winnerImage.get_rect()
            self.winnerImageRect.x, self.winnerImageRect.y = settings.screenWidth/2, settings.screenHeight/3
            self.screen.blit(self.winnerImage, self.winnerImageRect)

