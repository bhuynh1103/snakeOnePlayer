import pygame, sys
from snake import *
from food import *
from pygame.locals import *
from constants import *


pygame.init()
pygame.font.init()

# Creates screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Instantiates snake and food
snake = Snake(white)
food = Food(green)


# Based on what input is given, changes direction
def keyPressed(up, left, down, right, player):
    if event.type == KEYDOWN and event.key == up:
        player.dir(0, -1)
    elif event.type == KEYDOWN and event.key == left:
        player.dir(-1, 0)
    elif event.type == KEYDOWN and event.key == down:
        player.dir(0, 1)
    elif event.type == KEYDOWN and event.key == right:
        player.dir(1, 0)

    # DEBUG
    elif event.type == KEYDOWN and event.key == K_SPACE:
        player.addTotal()


def writeText(window, written, cenX, cenY, color):
    font = pygame.font.Font(None, int(scale * .66))
    text = font.render(written, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)


pause = False

# Game loop
while True:
    while not pause:
        # Controls FPS
        pygame.time.wait(100)

        # Draws background and border
        screen.fill(black)
        pygame.draw.rect(screen, gray(51), (0, 0, width, height), (scale * 2) - 1)

        snake.death(screen)
        snake.update()

        # Draws snake and food
        snake.draw(screen)
        food.draw(screen)

        # DEBUG
        # print(snake.tail, snake.total)

        # If snake is at same position as food, then it is 'eaten'
        if snake.eat(food.x, food.y):
            food.newXY()
            food.check(snake.tail)
            snake.total += 2
            snake.score += 1
            
        scoreText = "Score: " + str(snake.score) 
        highScoreText = "Highscore: " + str(snake.highscore)
        
        writeText(screen, scoreText, width * (1 / 3), scale // 2, black)
        
        if snake.score >= snake.highscore:
            snake.highscore = snake.score
            
        writeText(screen, highScoreText, width * (2 / 3), scale // 2, orange)

        # Updates screen
        pygame.display.update()

        # Quit loop and keyPressed checker
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            keyPressed(K_w, K_a, K_s, K_d, snake)

            # Checks if "P" is pressed, if so it pauses game
            if event.type == KEYDOWN and event.key == K_p:
                pause = True

    # Pause loop
    screen.fill(black)
    pygame.draw.rect(screen, yellow, (0, 0, width, height), (scale * 2) - 1)

    snake.draw(screen)
    food.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_p:
            pause = False
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
