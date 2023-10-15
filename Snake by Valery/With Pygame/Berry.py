'''
Данный класс описывает сущность ягодки. Имеет следующие методы:
-   отрисовка ягодки.
-   рандомная генерация в пределах поля
'''

import pygame
from pygame.math import Vector2
import random
import Field

class Berry:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x) * Field.cell_size, int(self.pos.y) * Field.cell_size, Field.cell_size, Field.cell_size)
        Field.screen.blit(Field.apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, Field.cell_number - 1)
        self.y = random.randint(0, Field.cell_number - 1)
        self.pos = Vector2(self.x, self.y)