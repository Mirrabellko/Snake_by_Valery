import random
'''
Данный класс описывает сущность Ягоды, содержит методы генерации новой ягодки
и проверки ее состояния
'''
X = 0
Y = 1

class Berry:
    def __init__(self, berry_coord: list, is_exist: bool):
        self.berry_coord = berry_coord
        self.is_exist = is_exist

    def new_berry(self, field_respawn: list, body_list: list):
        while True:
            coord = random.choice(field_respawn)
            if coord not in body_list:
                self.berry_coord = coord
                self.is_exist = True
                break
        return self.berry_coord

    def is_berry_exist(self):
        return self.is_exist
