# Attempt at creating a local two player pong game in the style of old tv game systems
import random
import pygame
pygame.init()
display_width = 800
display_height = 600
ball_size = 10
WHITE = (255, 255, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Python Pong')
background1 = pygame.image.load('background.png')
player1_bat = pygame.image.load('bat.png')
player2_bat = pygame.image.load('bat.png')
clock = pygame.time.Clock()


class Ball:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
      
        
def make_ball():
    ball = Ball()
    ball.x = random.randrange(ball_size, display_width - ball_size)
    ball.y = random.randrange(ball_size, display_height - ball_size)
    
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random .randrange(-2, 3)
    return ball   
    

def player1(x, y):
    gameDisplay.blit(player1_bat, (x, y))


def player2(x2, y2):
    gameDisplay.blit(player2_bat, (x2, y2))
                     

def game_loop():
  
    x = 1
    y = 200
    x2 = 784
    y2 = 200
    pone_y_change = 0
    ptwo_y_change = 0
    bat_height = 165
    gameExit = False
    ball_speed = 2

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ptwo_y_change = -5
                elif event.key == pygame.K_DOWN:
                    ptwo_y_change = 5
                elif event.key == pygame.K_w:
                    pone_y_change = -5
                elif event.key == pygame.K_s:
                    pone_y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ptwo_y_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    pone_y_change = 0
               
        y += pone_y_change
        y2 += ptwo_y_change
        gameDisplay.blit(background1, [0, 0])
              
        player1(x, y)
        player2(x2, y2)
        
        if y > display_height - bat_height or y < 0:
            pone_y_change = 0
        if y2 > display_height - bat_height or y2 < 0:
            ptwo_y_change = 0
        ball = make_ball()
        ball.x += ball.change_x
        ball.y += ball.change_y
        if ball.y > display_height - ball_size or ball.y < ball_size:
            ball.change_y *= -1
        if ball.x > display_width - ball_size or ball.x < ball_size:
            ball.change_x *= -1
        pygame.draw.circle(gameDisplay, WHITE, [ball.x, ball.y], ball_size)
        pygame.display.update()
        clock.tick(2)

        
game_loop()
pygame.quit()
quit()





