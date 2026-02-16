import pygame
import time
pygame.init()
x = 0
y = 0
screen = pygame.display.set_mode((1000, 720))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by David Nashed")

#Tuples containing the colours to be used in the game
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (188, 227, 199)

#Fonts for Game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()#sets speed of snake movement

quit_game = False

snake_x = 490 #Centre point horizontally is (1000-20 snake Width)/2 = 490
snake_y = 350 #Centre point vertically is (720-20 snake height)/2 = 350

#holds the value of changes in the coordinates

snake_x_change = 0
snake_y_change = 0

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20
    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green) #changes black screen to green



    #Create rectangle for Snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)#sets FPS

pygame.quit()
quit()
