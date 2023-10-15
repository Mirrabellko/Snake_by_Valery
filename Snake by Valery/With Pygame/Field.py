'''
Данный класс представляет основную логику игры.
Здесь содержатся следующие методы:
-   обновление состояния поля.
-   отрисовка элементов поля(змейка, ягодка и количество баллов).
-   проверка на "съедение" ягодки. И сразу же проверка, чтобы ягодка не
    сгенерировалась на теле змеи.
-   проверка на конец игры. Конец игры наступает в 2-х случаях: столкновение с
    границами поля или же столкновение головы с собственным телом
-   конец игры. Запускает стартовую генерацию сущности змейка.
-   отсчет и отрисовка количесва баллов

Через эту сущность осуществляется управление сущностями ягодки и змейки
'''

import pygame
import Snake
import Berry


pygame.init()
cell_size = 30      # В качестве констант обозначен размер поля. Можно менять
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake by Valery")
clock = pygame.time.Clock()
apple = pygame.image.load('berry_image.png').convert_alpha()
game_font = pygame.font.Font(None, 25)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

class Field:
    def __init__(self):
        self.snake = Snake.Snake()
        self.fruit = Berry.Berry()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_part()

        for i in self.snake.body[1:]:
            if i == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for i in self.snake.body[1:]:
            if i == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)