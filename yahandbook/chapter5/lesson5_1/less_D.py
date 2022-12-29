# Работа не волк
# import constants


class Programmer:
    JUN = 'Junior'
    MID = 'Middle'
    SEN = 'Senior'

    JUN_SAL = 10
    MID_SAL = 15

    def __init__(self, name, position, time=0, salary=0, sen_sal=20):
        self.name = name
        self.position = position
        self.time = time
        self.salary = salary
        self.sen_sal = sen_sal

    # Время
    def work(self, time):
        self.time = self.time + time
        self.salary += self.set_salary(time)

    # Оплата
    def set_rise(self):
        pos = self.get_position()
        if pos == self.JUN:
            return self.MID
        elif pos == self.MID:
            return self.SEN
        else:
            self.sen_sal += 1
            return self.sen_sal

    # Повышение
    def rise(self):
        self.position = self.set_rise()

    def get_position(self):
        return self.position

    # Оплата
    def set_salary(self, time):
        pos = self.get_position()
        if pos == self.JUN:
            return time * self.JUN_SAL
        elif pos == self.MID:
            return time * self.MID_SAL
        else:
            return time * self.sen_sal

    def info(self):
        return f'{self.name} {self.time}ч. {self.salary}тгр.'
