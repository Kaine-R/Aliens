from random import randint


class Settings():
    def __init__(self):

        #screen
        self.screenWidth = 1500
        self.screenHeight = 650
        self.bgColor = (20, 20, 20)

        # PLAYER
        self.playerSpeed = 1.6

        # AI
        self.AISpeed = .25

        # BALL
        self.ballSpeed = .3

        # SCORE LIMIT
        self.scoreLimit = 3
