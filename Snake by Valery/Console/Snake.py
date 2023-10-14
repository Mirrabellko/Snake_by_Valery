import random
import Berry

'''
Данный класс описывает сущность Змейка. В нем реализованы методы движения, генерации
новой змейки, проверки длины, съедание ягодки и проверка конца игры.

'''

X = 0           # Константа для координаты Х
Y = 1           # Константа для координаты Y
HEAD_INDEX = 0  # По умолчанию голова змейки будет на индексе 0

class Snake:
    def __init__(self, body_list: list, long=1):
        self.long = long
        self.body_list = body_list

    def get_head(self) -> list:
        return self.body_list[HEAD_INDEX]

    def new_snake(self, field_respawn: list):
        coord = random.choice(field_respawn)
        self.body_list.append(coord)

    def check_long(self):
        if self.long < len(self.body_list):
            self.body_list.pop(-1)

    def turn_left(self):
        coord = self.body_list[HEAD_INDEX][Y] - 1
        new_step = [self.body_list[HEAD_INDEX][X], coord]
        self.body_list.insert(HEAD_INDEX, new_step)
        self.check_long()

    def turn_up(self):
        coord = self.body_list[HEAD_INDEX][X] - 1
        new_step = [coord, self.body_list[HEAD_INDEX][Y]]
        self.body_list.insert(HEAD_INDEX, new_step)
        self.check_long()

    def turn_down(self):
        coord = self.body_list[HEAD_INDEX][X] + 1
        new_step = [coord, self.body_list[HEAD_INDEX][Y]]
        self.body_list.insert(HEAD_INDEX, new_step)
        self.check_long()

    def turn_right(self):
        coord = self.body_list[HEAD_INDEX][Y] + 1
        new_step = [self.body_list[HEAD_INDEX][X], coord]
        self.body_list.insert(HEAD_INDEX, new_step)
        self.check_long()

    def check_game_over(self):
        head = self.body_list[HEAD_INDEX]
        if self.body_list.count(head) == 3:
            return 'game over'

    def eat_berry(self, berry_coord: list):
        self.long += 1
        self.body_list.append(berry_coord)

    def snake_search_berry(self, berry_coord: list,):
        head = self.get_head()
        if head[X] < berry_coord[X]:
            self.turn_down()
        elif head[X] == berry_coord[X]:
            if head[Y] > berry_coord[Y]:
                self.turn_left()
            elif head[Y] == berry_coord[Y]:
                self.eat_berry(berry_coord)
                return False
            else:
                self.turn_right()
        else:
            self.turn_up()









