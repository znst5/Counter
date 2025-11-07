import emoji

class Employee:
    def __init__(self, name, age, position, bonus):
        self.name = name
        self.age = age
        self.position = position
        self.bonus = bonus
    def __str__(self):
        return f'(Имя:{self.name}, Возраст:{self.age}, Должность:{self.position}, Премия:{self.bonus})'


if __name__ == '__main__':
    e = Employee('Data', 23, 'worker', 1000)
    print(e, emoji.emojize(':red_heart: :man_office_worker:'))