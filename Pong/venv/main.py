import pygame
from pygame.sprite import Group
from settings import Settings
from gameStats import GameStats
from button import Button
from player import Player
from ai import AI
from ball import Ball
from scoreBoard import ScoreBoard
from menu import Menu
import gameFunctions as gf


def runGame():
    pygame.init()
    pygame.display.set_caption("Pong")
    settings = Settings()
    gameStats = GameStats()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    menu = Menu()
    button = Button(screen, settings, "Play")
    scores = ScoreBoard(screen, settings, gameStats)
    player = Player(screen, settings)
    bot = AI(screen, settings, menu)
    balls = Group()
    newBall = Ball(screen, settings, menu)
    balls.add(newBall)


    while True:
        screen.fill(settings.bgColor)
        gf.drawField(screen, settings)
        gf.checkEvent(player, settings, menu, gameStats, scores, button)
        gf.updateScreen(player, balls, bot, scores)

        if gameStats.gameActive == True:
            player.update()
            bot.update(balls)
            balls.update(settings, gameStats, scores, balls)
            scores.showScore()
            gf.checkBallAmount(screen, settings, bot, balls, menu)

            if gameStats.playerScore >= settings.scoreLimit or gameStats.botScore >= settings.scoreLimit:
                gf.restartGame(screen, settings, gameStats, player, bot, balls, menu)

        if gameStats.gameActive == False:
            button.drawButton()
            pygame.mouse.set_visible(True)
            menu.drawWin(gameStats, settings)
            menu.prepMenu(screen, settings, balls, bot)
            menu.drawMenu()


        pygame.display.flip()


runGame()