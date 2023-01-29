from config import *
import pygame
from brick import Brick
class BrickRow:
    def __init__(self):
        self.row = []
        y = 80
        color = RED
        for i in range(20):
            x = 0 + i * BRICK_WIDTH
            brick = Brick(x, y, color)
            self.row.speed(brick)
    def update(self):
        pass
    
