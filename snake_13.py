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
blue = (0,0,255)
dark_green = (0, 153, 51)
#Fonts for Game
score_font = pygame.font.SysFont("snake chan.ttf", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)

clock = pygame.time.Clock()#sets speed of snake movement

#function for highscore
def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value

#Display player score
def player_score(score, score_colour):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (900,20)) #coords for top right

def draw_snake(snake_list):
    # print(f"Snake list: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, dark_green, [i[0], i[1], 20, 20])

def game_loop():

    quit_game = False
    game_over = False
    snake_x = 480 #Centre point horizontally is (1000-20 snake Width)/2 = 480
    snake_y = 340 #Centre point vertically is (720-20 snake height)/2 = 340

    #holds the value of changes in the coordinates

    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1
    #set random position for food
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    #Loads high score
    high_score = load_high_score()
    print(f"high_score test: {high_score}") #TEST

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

        #keeping score
        score = snake_length - 1
        player_score(score, black)


        #link speed of snake to player score to increase difficulty
        if score > 3:
            speed = score
        else:
            speed = 3
        #Create circle for Food
        food = pygame.Rect(food_x, food_y, 20,20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20,20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        #Collision detection (test snake touch food)
        if snake_x == food_x and snake_y == food_y:
            #set new position for food when touched
            food_x = round(random.randrange(20,1000 - 20) / 20) * 20
            food_y = round(random.randrange(20,720 - 20) / 20) * 20
            print("Got it!")
            #increase snake length
            snake_length += 1

        clock.tick(speed)#sets FPS


    pygame.quit()
    quit()
#Main Routine
game_loop()
