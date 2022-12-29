# Работа не волк

class Programmer:

    JUN = 'Junior'
    MID = 'Middle'
    SEN = 'Senior'

    def __init__(self, name, position, salary=0):
        self.name = name
        self.position = position
        self.salary = salary

    def work(self, time):
        pass

    def rise(self):
        if self.position == self.JUN:
            self.position = self.MID
        elif self.position == self.MID:
            self.position = self.SEN
        else:
            self.salary += 1

    def info(self):
        pass
