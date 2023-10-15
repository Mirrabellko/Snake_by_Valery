'''
Данный класс описывает сущность змейка, имеет следующие методы:
-   отрисовка змейки. Змейка изначально создается на стартовых координатах,
    тело состоит из 3-х блоков
-   передвижение змейки. Стартовое положение закреплено,
    движение наступает лишь когда пользователь нажимает кнопку
-   добавление новой части тела змейки. Если произошло событие "съедания ягодки",
    то поле "new_part" сигнализирует о том, что нужно тело змеи увеличить
-   сброс полей змейки до стартового состояния. Вызывается при соприкосновении
    змейки с самой собой или границами поля
'''

import pygame
from pygame.math import Vector2
import Field


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_part = False

    def draw_snake(self):
        for i in self.body:
            x_pos = int(i.x * Field.cell_size)
            y_pos = int(i.y * Field.cell_size)
            part_rect = pygame.Rect(x_pos, y_pos, Field.cell_size, Field.cell_size)
            pygame.draw.rect(Field.screen, (183, 111, 122), part_rect)

    def move_snake(self):
        if self.new_part == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_part = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_part(self):
        self.new_part = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)