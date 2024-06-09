from board import boards
import pygame
import math

pygame.init()



# the width and height for the bord in game
WIDTH = 900
HEIGHT = 950
secreen = pygame.display.set_mode((WIDTH, HEIGHT)) # secreen : the secreen in game
timer = pygame.time.Clock() # the speed it will game runs
fps = 60 # the max speed in the game
front = pygame.font.Font('freesansbold.ttf', 20) # the score , game over , start
level = boards
color = 'blue'
PI = math.pi
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))

player_x = 450
player_y = 663
direction = 0
counter = 0
# function will convert numbers to images
def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)

    for i in range(len(level)):
        for j in range(len(level[i])):

            if level[i][j] == 1:
                # 1- where it will be 2- color 3-x and y 4- size
                pygame.draw.circle(secreen,"white",(j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(secreen, "yellow", (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 12)
            if level[i][j] == 3:
                # 1- where it will be 2- color 3- start post 4- end pos 4- width
                pygame.draw.line(secreen,color,(j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1 ), 3)
            if level[i][j] == 4:
                pygame.draw.line(secreen, color, (j * num2, i * num1 + (0.5 * num2)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                # we use the math.pi where circle start and end
                pygame.draw.arc(secreen,color,[(j*num2 - (num2 * 0.4))-2, (i * num1 + (num1 * 0.5)), num2, num1], 0, PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(secreen,color,[(j*num2 + (num2 * 0.5)), (i * num1 + (num1 * 0.5)), num2, num1], PI /2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(secreen,color,[(j*num2 + (num2 * 0.5)), (i * num1 - (num1 * 0.4)), num2, num1], PI, 3 * PI/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(secreen,color,[(j*num2 - (num2 * 0.4)), (i * num1 - (num1 * 0.4)), num2, num1], 3 * PI/2, 2*PI, 3)

            if level[i][j] == 9:
                pygame.draw.line(secreen, 'red', (j * num2, i * num1 + (0.5 * num2)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def draw_player():
    if direction == 0:
        # 5 is for Control the animation speed of the player
        secreen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        secreen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        secreen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        secreen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


# game loop
run = True
# while game run
while run:
    timer.tick(fps)
    # Control the animation speed of the player
    if counter < 19:
        counter += 1
    else:
        counter = 0

    secreen.fill('black')
    draw_board()
    draw_player()

    # when game will be to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # make pac-man moving in up, down, right and left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3



    pygame.display.flip()
pygame.quit()