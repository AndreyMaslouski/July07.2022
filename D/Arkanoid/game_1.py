import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
fps = 60

# paddle settings
paddle_w = 300
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w//2,HEIGHT - paddle_h - 10, paddle_w, paddle_h)
#ball settings
ball_radius = 20
ball_speed = 6
ball_rect = int(str(ball_radius) * 2 ** 0,5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2,ball_rect,ball_rect)
dx, dy = 1,-1

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

#background image
img = pygame.image.load('1.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img,(0,0))
    #drawing world
    pygame.draw.rect(sc,pygame.Color('darkorange'), paddle)
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
    # ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    # update screen
    pygame.display.flip()
    clock.tick(fps)