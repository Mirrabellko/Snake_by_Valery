import Snake
import Field
import Berry

import time


"""
Игрок может указывать размер поля в начале игры.
Здесь содержится создание основных сущностей, вызов методов генерация поля, 
и основной цикл игры
"""

FIELD_SIZE = int(input("Input size of field you need: "))

if __name__ == "__main__":
    game = 'new'
    field = Field.Field(FIELD_SIZE)         # Создание сущности поля
    field.make_coord_list(FIELD_SIZE)
    field.make_field_border(FIELD_SIZE)
    field.make_field_respawn(FIELD_SIZE)
    snake = Snake.Snake([], 1)              # Создание сущности змейки
    snake.new_snake(Field.field_respawn)
    berry = Berry.Berry([0, 0], False)      # Создание сущности ягодка
    berry.new_berry(Field.field_respawn, snake.body_list)
    berry_status = berry.is_berry_exist()
    field.view_game(Field.coord_matrix, snake.body_list, Field.field_border, berry.berry_coord)

    while game != 'game over':
        field.clear_field()
        berry_status = snake.snake_search_berry(berry.berry_coord)
        if berry_status == False:
            berry.new_berry(Field.field_respawn, snake.body_list)
        game = snake.check_game_over()
        field.view_game(Field.coord_matrix, snake.body_list, Field.field_border, berry.berry_coord)
        print(f'Your score: {snake.long - 1}')
        time.sleep(0.2)