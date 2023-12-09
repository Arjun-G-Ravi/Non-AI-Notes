import pygame

# Always initialise
pygame.init()

# To make a screen
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Space invadors")
# pygame.display.set_icon(pygame.image.load('10_Pygame learn/01_Space Invaders /spaceship.png')) # wont wprk in ubuntu

running = True
playerImg = pygame.image.load('./spaceship.png')
player_pos = [400,500]
go_left = False
go_right = False

def player(x,y):
    screen.blit(playerImg, player_pos)

while running:
    # fill screen with black
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                go_left = True
                go_right = False 
    
            if event.key == pygame.K_RIGHT:
                go_right = True
                go_left = False
                
        if event.type == pygame.KEYUP:
            go_left = False
            go_right = False
    
    if go_left:
        if player_pos[0] > 10:
            player_pos[0] -= 10
    
    if go_right:
        if player_pos[0] < 750:
            player_pos[0] += 10
    
    
    
     
    # place player(spaceship) at player_pos
    player(player_pos[0], player_pos[1])

    # This is where the screen gets updated with the above changes
    pygame.display.update()

    # A clock adjusts frame rate
    pygame.time.Clock().tick(60)












