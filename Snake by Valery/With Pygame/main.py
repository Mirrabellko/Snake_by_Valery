'''
Здесь содержится основной цикл игры.
Связь с сущностями осуществляется через сущность поля
'''

import sys
import pygame
import Field

from pygame.math import Vector2


main_game = Field.Field()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # Прописан выход по кнопке выхода
            pygame.quit()
            sys.exit()
        if event.type == Field.SCREEN_UPDATE:   # Обновление экрана
            main_game.update()
        if event.type == pygame.KEYDOWN:        # Прописаны кнопки для движения змейки
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    Field.screen.fill(pygame.Color(175, 215, 70))     # Цвет фона поля
    main_game.draw_elements()                         # Отрисовка сущностей
    pygame.display.update()                           # Стандартный метод для обновления экрана
    Field.clock.tick(60)                              # Количество кадров в минуту. Можно менять
