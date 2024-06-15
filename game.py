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
blinky_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45)))
pinky_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45)))
inky_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45)))
clyde_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45)))
spooked_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45)))
dead_img = player_images.append(pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45)))
player_x = 450
player_y = 663
direction = 0

blinky_x = 56
blinky_y = 58
blinky_direction = 0

pinky_x = 440
pinky_y = 388
pinky_direction = 2

inky_x = 440
inky_y = 438
inky_direction = 2

clyde_x = 440
clyde_y = 438
clyde_direction = 2

counter = 0
flicker = False
# can i go L R U D
turns_allowed = [False, False ,False, False]
direction_command = 0
player_speed = 2
ghost_speed = 2
score = 0
monster_up = False
monster_counter = 0
eaten_ghosts = [False, False, False, False]

targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]\

blinky_dead = False
pinky_dead = False
inky_dead = False
clyde_dead = False

blinky_box = False
pinky_box = False
inky_box = False
clyde_box = False
moving = False
startup_counter = 0
lives = 3

class Ghost:
    def __init__(self, x, y, target, speed, img, direct, dead, box, id):
        self.x_pos = x
        self.y_pos = y
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()

    def draw(self):
        if (not monster_up and not self.dead) or (eaten_ghosts[self.id] and monster_up and not self.dead):
            secreen.blit(self.img, (self.x_pos, self.y_pos))
        elif monster_up and not self.dead and not eaten_ghosts[self.id]:
            secreen.blit(spooked_img, (self.x_pos, self.y_pos))
        else:
            secreen.blit(dead_img, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect(self.x_pos - 18, self.y_pos - 18, (36, 36))
        return ghost_rect

    def check_collisions(self):
        return self.turns, self.in_box

def check_collisions(points, monster, monster_count, eaten_ghost):
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    if 0 < player_x < 870:
        if level[center_y // num1][center_x // num2] == 1:
            level[center_y // num1][center_x // num2] = 0
            points += 10
        if level[center_y // num1][center_x // num2] == 2:
            level[center_y // num1][center_x // num2] = 0
            points += 50
            monster = False
            monster_count = 0
            eaten_ghost = [False, False, False, False]

    return points, monster, monster_count, eaten_ghost

def draw_misc():
    score_text = front.render(f'Score: {score}', True, 'white')
    secreen.blit(score_text, (10, 920))
    if monster_up:
        pygame.draw.circle(secreen, 'blue', (140,930),15)
    for i in range(lives):
        secreen.blit(pygame.transform.scale(player_images[0], (30, 30)), (650 + i * 40, 915))


# function will convert numbers to images
def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)

    for i in range(len(level)):
        for j in range(len(level[i])):

            if level[i][j] == 1:
                # 1- where it will be 2- color 3-x and y 4- size
                pygame.draw.circle(secreen,"white",(j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2 and not flicker:
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
                pygame.draw.line(secreen, 'white', (j * num2, i * num1 + (0.5 * num2)),
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


def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (HEIGHT - 50) // 32
    num2 = (WIDTH // 30)
    num3 = 15

    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1: # basil please Don't get distracted. It took four hours to figure out the problem
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True
    return turns



def move_player(play_x,play_y):
    if direction == 0 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        play_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y



# game loop
run = True
# while game run
while run:
    timer.tick(fps)
    # Control the animation speed of the player
    if counter < 19:
        counter += 1
        if counter > 4:
            flicker = False
    else:
        counter = 0
        flicker = True
    if monster_up and monster_counter < 600:
        monster_counter +=1
    elif monster_up and monster_counter >= 600:
        monster_counter = 0
        monster_up = False
        eaten_ghosts = [False, False, False, False]
    if startup_counter < 180:
        moving = False
        startup_counter +=1
    else:
        moving = True


    secreen.fill('black')
    draw_board()
    draw_player()
    blinky = Ghost(blinky_x, blinky_y, targets[0], ghost_speed, blinky_img,
                   blinky_direction, blinky_dead, blinky_box, 0)
    inky = Ghost(inky_x, inky_y, targets[1], ghost_speed, inky_img,
                 inky_direction, inky_dead, inky_box, 1)
    pinky = Ghost(pinky_x, pinky_y, targets[2], ghost_speed, pinky_img,
                 pinky_direction, pinky_dead, pinky_box, 2)
    clyde = Ghost(clyde_x, clyde_y, targets[3], ghost_speed, clyde_img,
                 clyde_direction, clyde_dead, clyde_box, 3)

    draw_misc()
    center_x = player_x + 23
    center_y = player_y + 24
    turns_allowed = check_position(center_x, center_y)
    if moving:
        player_x, player_y = move_player(player_x, player_y)
    score, monster, monster_counter, eaten_ghosts = check_collisions(score, monster_up, monster_counter, eaten_ghosts)

    # when game will be to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # make pac-man moving in up, down, right and left
        if event.type == pygame.KEYDOWN:
            # the keys in keyboard to let pacman move
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction

    for i in range(4):
        if direction_command == i and turns_allowed[i]:
            direction = i


        if player_x > 900:
            player_x = -47
        elif player_x < -50:
            player_x = 897





    pygame.display.flip()
pygame.quit()