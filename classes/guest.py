
class Guest:

    def __init__(self, age, cash, name):
        self.age = age
        self.cash = cash
        self.name = name
           
    def reduce_cash(self,amount):
        self.cash -= amount
