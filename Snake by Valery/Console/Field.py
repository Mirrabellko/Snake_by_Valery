import os

'''
Данный класс описывает сущность Поля. Содержит такие поля: установка размера поля, 
отрисовка игры, очистка экрана, а так же генераторы координат для поля.
'''
X = 0           # Константа для координаты Х
Y = 1           # Константа для координаты Y

coord_matrix = []      # Список координат, которые у нас будут в рамках размера поля
field_border = []      # Границы поля, которые не будут учитываться в генерировании и передвижении
field_respawn = []     # Список координат, которые будут использоваться при генерировании

class Field:
    def __init__(self, size: int):
        self.size = size

    def set_size(self, field_size: int):
        self.size = field_size

    def view_game(self, coord_matrix: list, last_step: list, field_border: list, berry_coord: list):
        for i in range(self.size):
            for j in range(self.size):
                if coord_matrix[i][j] in last_step:
                    print("*", end="\t")
                elif coord_matrix[i][j] in field_border:
                    print("=", end="\t")
                elif i == berry_coord[X] and j == berry_coord[Y]:
                    print("O", end="\t")
                else:
                    print(" ", end="\t")
            print()

    def clear_field(self):
        os.system("cls")
        print()

    def make_coord_list(self, field_size: int):
        for i in range(field_size):
            coord_matrix.append([])
            for j in range(field_size):
                coord_matrix[i].append([i, j])

    def make_field_border(self, field_size: int):
        for i in range(field_size):
            for j in range(field_size):
                if i == 0 or i == field_size - 1:
                    field_border.append([i, j])
                if j == 0 or j == field_size - 1:
                    field_border.append([i, j])

    def make_field_respawn(self, field_size: int):
        for i in range(1, field_size-1):
            for j in range(1, field_size-1):
                field_respawn.append([i, j])