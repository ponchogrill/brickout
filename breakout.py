import pygame
import sys
from config import *
from ball import Ball
from brick import Brick
from brickrow import BrickRow
# здесь определяются константы,
# классы и функции
def point_in_rect(pointx, pointy, rectx, recty, rect_width, rect_height):
    inx = rectx <= pointx <= rectx + rect_width
    iny = recty <= pointy <= recty + rect_height
    return inx and iny

# здесь происходит инициация,
# создание объектов
ball = Ball()
pygame.init()
brick = Brick(50, 50, RED)
brock = Brick(50, 50, RED)
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
#координаты ракетки

bat_x = BAT_OFFSET 
bat_y = 970
f2 = pygame.font.SysFont('algerian', 48)
#скорость ракетки
bat_speed_x = 0
#score
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # --------
    # изменение объектов
    # --------
    ball.update()  
     #правая   
    keys = pygame.key.get_pressed()
    bat_x +=bat_speed_x
    if keys[pygame.K_LEFT]:
        bat_x -= 10
    elif keys[pygame.K_RIGHT]:
        bat_x += 10
    if bat_x <= 0:
        bat_x = 0
    elif bat_x >= SCREEN_WIDTH - BAT_WIDTH:
        bat_x = SCREEN_WIDTH - BAT_WIDTH
    #проверяем что мяч попал в ракетку
    #вычисляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx = ball.x - ball.r
    mid_lefty = ball.y
    
    mid_rightx = ball.x + ball.r
    mid_righty = ball.y
    
    mid_topx = ball.x
    mid_topy = ball.y - ball.r

    mid_bottomx = ball.x
    mid_bottomy = ball.y + ball.r
    #правая граница ракетки
    if point_in_rect(mid_leftx, mid_lefty, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y        
    #левая граница ракетки
    if point_in_rect(mid_leftx, mid_lefty, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y   
  
     #верхняя граница ракетки
    if point_in_rect(mid_bottomx, mid_bottomy, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball.speed_y = -ball.speed_y
    #score
    score_left_text = f2.render(str(ball.left_score), True,
                  (255, 180, 0))         
    # ОТРИСОВКА экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball.x, ball.y), ball.r)
    pygame.draw.rect(sc, ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    sc.blit(score_left_text, (SCREEN_WIDTH//2 - 100, 10))
    pygame.draw.rect(sc, brick.color, (brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT))
    for brick in brick_row.row:
        pygame.draw.rect(sc, brick.color, (brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT), 1)
        pygame.draw.rect(sc, brick.color, (brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT))
    #score
    pygame.display.update()
