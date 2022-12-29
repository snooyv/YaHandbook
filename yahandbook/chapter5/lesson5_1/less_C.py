# Не нажимай крассную кнопку

class RedButton:

    def __init__(self, clk_cnt=0):
        self.clk_cnt = clk_cnt

    def click(self):
        print("Тревога!")
        self.clk_cnt += 1

    def count(self):
        return self.clk_cnt
