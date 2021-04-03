import pygame, sys, random

# initialise all pygame functions
pygame.init()

# Define variables for colours in (r,g,b) format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define variables for the screen size
screenWidth = 500
screenHeight = 500

window = pygame.display.set_mode((screenWidth, screenHeight))

# create a clock to help control the display window update
clock = pygame.time.Clock()

# window refresh speed
speed = 15

# Define starting positions for the box in the game window
xPos = 250
yPos = 250

# Define box size (width, height)
wBox = 10
hBox = 10

# box will move in the x and y directions each loop cycle
xMove = 0
yMove = 0

xApple = random.randint(0, 49) * 10
yApple = random.randint(0, 49) * 10

snake = [[xPos, yPos]]

# Define a variable to control whether the game loop should run
runGame = True
while runGame == True:

    # Check to see if there has been a key press or
    # mouse click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # exit while loop on next cycle
            runGame = False
        else:
            # Check the arrow keys for a direction change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # make xMove -ve to move left
                    xMove = -wBox
                    # no move up or down, yMove = 0
                    yMove = 0
                if event.key == pygame.K_UP:
                    # make yMove -ve to move up
                    yMove = -hBox
                    # no move left or right, xMove = 0
                    xMove = 0
                if event.key == pygame.K_RIGHT:
                    # make xMove +ve to move right
                    xMove = wBox
                    # no move up or down, yMove = 0
                    yMove = 0
                if event.key == pygame.K_DOWN:
                    # make xMove +ve to move down
                    yMove = hBox
                    # no move left or right, xMove = 0
                    xMove = 0

                if event.key == pygame.K_f:
                    xApple = random.randint(0, 49) * 10
                    yApple = random.randint(0, 49) * 10

    snake.append([xPos, yPos])
    snake = snake[1:]

    # update XPos and yPos using xMove and yMove
    xPos = xPos + xMove
    yPos = yPos + yMove

    # Check if the box touches a boundary, and if so
    # change the sign (+ve/-ve -> -ve/+ve) of xMove/yMove
    # so the box appears to 'bounce' off the boundary
    if xPos == 0:
        xMove = wBox
    if xPos == screenWidth - wBox:
        xMove = -wBox
    if yPos == 0:
        yMove = hBox
    if yPos == screenHeight - hBox:
        yMove = -hBox

    # clear the game window, then draw the red square
    # at the location xPos, tPos
    if xPos == xApple and yPos == yApple:
        xApple = random.randint(0, 49) * 10
        yApple = random.randint(0, 49) * 10
        snake.append([xPos, yPos])

    window.fill(BLACK)
    pygame.draw.rect(window, GREEN, (xApple, yApple, wBox, hBox))
    for seg in snake:
        pygame.draw.rect(window, RED, (seg[0], seg[1], wBox, hBox))

    pygame.display.update()

    clock.tick(speed)
