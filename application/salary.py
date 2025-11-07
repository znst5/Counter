import emoji
from db.people import Employee

class Salary(Employee):
    def __init__(self, name, age, position, salary, percent, bonus):
        self.salary = salary
        self.percent = percent
        super().__init__(name, age, position, bonus)

    def get_salary(self):
        tax = (self.salary + self.bonus) * self.percent / 100
        sum_ = self.salary + self.bonus - tax

        return sum_

    def __str__(self):
        return f'(Имя:{self.name}, Зарплата:{sum_})'


s = Salary('Data', 23, 'worker', 1000, 13, 1000 )
print(s)

# if __name__ == '__main__':