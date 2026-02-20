import pygame
import time
import random

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
yellow = (255, 255, 0)

#Fonts for Game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)

clock = pygame.time.Clock()#sets speed of snake movement

def draw_snake(snake_list):
    print(f"Snake list: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])

def game_loop():

    quit_game = False
    game_over = False
    snake_x = 490 #Centre point horizontally is (1000-20 snake Width)/2 = 490
    snake_y = 350 #Centre point vertically is (720-20 snake height)/2 = 350

    #holds the value of changes in the coordinates

    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1
    #set random position for food
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20


    while not quit_game:
        while game_over:
            screen.fill(white)
            message("You lost Bozo! Press 'Q' to Quit or 'A' to play Again",
                    black, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()#restart main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit, Space to Resume, R to Reset"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        #If user presses X, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()
                            if event.key == pygame.K_SPACE:
                                end = True

                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True


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
        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y <0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green) #changes black screen to green

        #Create rectangle for Snake
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        draw_snake(snake_list)

        pygame.display.update()

        #Create circle for Food
        pygame.draw.circle(screen,yellow,[food_x,food_y], 10)
        pygame.display.update()

        #print lines for testing
        print(f"Snake x: {snake_x}")
        print(f"Food x: {food_x}")
        print(f"Snake y: {snake_y}")
        print(f"Food y: {food_y}")
        print("f\n\n")

        #Collision detection (test snake touch food)
        if snake_x == food_x - 10 and snake_y == food_y - 10:
            #set new position for food when touched
            food_x = round(random.randrange(20,1000 - 20) / 20) * 20
            food_y = round(random.randrange(20,720 - 20) / 20) * 20

            #increase snake length
            snake_length += 1

        clock.tick(5)#sets FPS


    pygame.quit()
    quit()
#Main Routine
game_loop()
