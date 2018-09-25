from person import Person

class Manager(Person):
    """
    Inherits from Person and defaults to give a 10% bonus
    for the giveRaise function
    """

    def giveRaise(self, percent, bonus = 0.10):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(0.20)
    print(tom.pay)
