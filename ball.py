from config import *

class Ball:
    def __init__(self):
        self.r = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = 5
        self.speed_y = 4
        self.left_score = 0
        self.right_score = 0

    def update(self):
        # передвигаем мяч по экрану
        self.x += self.speed_x
        self.y += self.speed_y
        # Выход за края экрана
        # левый
        if self.x <= self.r:
            # летел налево - полетел направо
            self.speed_x = -self.speed_x
            self.right_score += 1        
        # правый
        if self.x >= SCREEN_WIDTH - self.r:
            # летел направо - полетел налево
            self.speed_x = -self.speed_x          
        #верхний
        if self.y <= self.r:
            self.speed_y = -self.speed_y
        #нижний
        if self.y >= SCREEN_HEIGHT - self.r:
            self.speed_y = -self.speed_y  
            self.left_score += 1
            self.x = 800
            self.y = 500
