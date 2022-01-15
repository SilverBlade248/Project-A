import pygame
from sys import exit

pygame.init()

width, length = ((900, 700))
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption('project_a')

clock = pygame.time.Clock()

colour = (255, 0, 0)
vel = 10
x = 450
y = 300

walkright = [pygame.image.load('Run (1).png'),pygame.image.load('Run (2).png'),pygame.image.load('Run (3).png'),pygame.image.load('Run (4).png'),pygame.image.load('Run (5).png'),pygame.image.load('Run (6).png')]
walkleft = [pygame.image.load('Runleft (4).png'),pygame.image.load('Runleft (5).png'),pygame.image.load('Runleft (6).png'),pygame.image.load('Runleft (7).png'),pygame.image.load('Runleft (8).png'),pygame.image.load('Runleft (9).png')]
idlestand = [pygame.image.load('Idle (1).png'),pygame.image.load('Idle (2).png'),pygame.image.load('Idle (3).png'),pygame.image.load('Idle (4).png'),pygame.image.load('Idle (5).png'),pygame.image.load('Idle (6).png')]

left = False
right = False
idle = True
dash = False

walkcount = 0 
idlecount = 0
jumpvel = 15
isjump = False

def redrawGameWindow():
    global walkcount
    global idlecount
    screen.fill((0, 0, 0))
    
    if walkcount + 1 >= 18:
        walkcount = 0
    
    if idlecount + 1 >= 18:
        idlecount = 0

    if right:
        screen.blit(walkright[walkcount//3], (x,y))
        walkcount += 1
    elif left:
        screen.blit(walkleft[walkcount//3], (x,y))
        walkcount += 1
    else: 
        screen.blit(idlestand[idlecount//3], (x,y))
        idlecount += 1
    pygame.display.update()

#Game Loop

running = True
while running:

    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 700:
        x += vel
        right = True
        left = False
        

    elif keys[pygame.K_LEFT] and x > -200:
        x -= vel
        left = True
        right = False
    else:
        right = False
        left = False
        walkcount = 0
        dash = False

    if isjump == False and keys[pygame.K_UP]:
        isjump = True

    if isjump == True:
        y -= jumpvel * 3
        jumpvel -= 1

        if jumpvel < -15:
            isjump = False
            jumpvel = 15

    if keys[pygame.K_RETURN] and dash == False:
        if left:
            x -= 100
            dash = True

        elif right:
            x += 100
            dash = True
            
        else:
            dash = False
            

    redrawGameWindow()

