import sys
import pygame
from player import Player
from ai import AI
from ball import Ball
from button import Button
from scoreBoard import ScoreBoard
from menu import Menu
from pygame.mixer import music



def checkEvent(player, settings, menu, gameStats, scores, button):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           checkKeyDown(event, player)
        elif event.type == pygame.KEYUP:
           checkKeyUp(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlay(gameStats, settings, menu, button, scores, mouseX, mouseY)
            checkMenu(gameStats, settings, menu, mouseX, mouseY)
        elif event.type == pygame.QUIT:
            sys.exit()


def checkKeyDown(event, player):
    if event.key == pygame.K_DOWN:
        player.movingDown = True
    elif event.key == pygame.K_UP:
        player.movingUp = True
    elif event.key == pygame.K_LEFT:
        player.movingLeft = True
    elif event.key == pygame.K_RIGHT:
        player.movingRight = True


def checkKeyUp(event, player):
    if event.key == pygame.K_DOWN:
        player.movingDown = False
    elif event.key == pygame.K_UP:
        player.movingUp = False
    elif event.key == pygame.K_LEFT:
        player.movingLeft = False
    elif event.key == pygame.K_RIGHT:
        player.movingRight = False

def checkMenu(gameStats, settings, menu, mouseX, mouseY):
    if menu.pointMoreImageRect.collidepoint(mouseX, mouseY):
        settings.scoreLimit += 1
    elif menu.pointLessImageRect.collidepoint(mouseX, mouseY):
        settings.scoreLimit -= 1
    elif menu.diffOpt1ImageRect.collidepoint(mouseX, mouseY):
        menu.difficulty = 0
    elif menu.diffOpt2ImageRect.collidepoint(mouseX, mouseY):
        menu.difficulty = 1
    elif menu.diffOpt3ImageRect.collidepoint(mouseX, mouseY):
        menu.difficulty = 2

def checkPlay(gameStats, settings, menu, button, scores, mouseX, mouseY): # Checks to see if play was pressed when gameActive is False
    if button.rect.collidepoint(mouseX, mouseY) and settings.scoreLimit > 0:
        gameStats.gameActive = True
        pygame.mouse.set_visible(False)
        scores.prepScore(gameStats)
        addDiff(settings, menu)
        menu.first = False


def checkBallAmount(screen, settings, bot, balls, menu):
    if len(balls) == 0:
        newBall = Ball(screen, settings, menu)
        balls.add(newBall)
        bot.closeBall.x = settings.screenWidth

def updateScreen(player, balls, bot, scores): # updates Player, bot, and balls (also tests for collisions
    player.drawPlayer()
    bot.drawAI()
    scores.showScore()
    checkBallCollision(balls, player, bot)

    for ball in balls.sprites():
        ball.drawBall()


def checkBallCollision(balls, player, bot):
    for ball in balls.sprites():
        if ball.rect.right >= player.rect.left and ball.rect.right <= player.rect.right: # Checks for Collision
            if ball.y + ball.size >= player.rect.top and ball.y <= player.rect.bottom:
                if ball.movingLeft == False: # this is so the ball only gets one speed boost per hit
                    ball.varience += 0.05
                    pygame.mixer.music.load('bounce.mp3')
                    pygame.mixer.music.play(0)
                ball.movingLeft = True
        if ball.rect.top == player.rect2.bottom or ball.rect.bottom == player.rect3.top:
            if (ball.rect.left <= player.rect2.right and ball.rect.right >= player.rect2.left) or (ball.rect.left <= player.rect3.right and ball.rect.right >= player.rect3.left):
                if ball.movingUp == False:
                    ball.movingUp = True
                else:
                    ball.movingUp = False
                ball.varience += 0.05
                pygame.mixer.music.load('bounce.mp3')
                pygame.mixer.music.play(0)

        if ball.rect.left >= bot.rect.left and ball.rect.left <= bot.rect.right: # Checks for Collision
            if ball.y + ball.size >= bot.rect.top and ball.y <= bot.rect.bottom:
                if ball.movingLeft == True: # this is so the ball only gets on speed boost per hit
                    ball.varience += 0.05
                    pygame.mixer.music.load('bounce.mp3')
                    pygame.mixer.music.play(0)
                ball.movingLeft = False
        if ball.rect.top == bot.rect2.bottom or ball.rect.bottom == bot.rect3.top:
            if (ball.rect.left <= bot.rect2.right and ball.rect.right >= bot.rect2.left) or (ball.rect.left <= bot.rect3.right and ball.rect.right >= bot.rect3.left):
                if ball.movingUp == False:
                    ball.movingUp = True
                else:
                    ball.movingUp = False
                ball.varience += 0.05
                pygame.mixer.music.load('bounce.mp3')
                pygame.mixer.music.play(0)

def restartGame(screen, settings, gameStats, player, bot, balls, menu):
    print("GAME RESET")
    gameStats.gameActive = False
    gameStats.playerScore = 0
    gameStats.botScore = 0
    player.reset()
    bot.reset()
    balls.empty()
    newBall = Ball(screen, settings, menu)
    balls.add(newBall)
    subDiff(settings, menu)

def drawField(screen, settings):
    pointList = (50, 55), (settings.screenWidth - 50, 55), (settings.screenWidth - 50, settings.screenHeight - 45), (50, settings.screenHeight - 45)
    pygame.draw.line(screen, (50, 50, 50), (settings.screenWidth/2, 0), (settings.screenWidth/2, settings.screenHeight), 5)
    pygame.draw.lines(screen, (50, 50, 50), True, pointList, 5)

def addDiff(settings, menu):
    if menu.difficulty == 1:
        settings.AISpeed += .15
        settings.ballSpeed += .1
    elif menu.difficulty == 2:
        settings.AISpeed += .3
        settings.ballSpeed += .2

def subDiff(settings, menu):
    if menu.difficulty == 1:
        settings.AISpeed -= .15
        settings.ballSpeed -= .1
    elif menu.difficulty == 2:
        settings.AISpeed -= .3
        settings.ballSpeed -= .2
