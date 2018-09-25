class Person:
    """
    Representation of a person in the database
    """
    def __init__(self, name, age, pay = 0, job = None):
        """
        Initialize a person object
        """
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        """
        Specify how to print the object
        """
        return ('<%s => %s: %s, %s>' %
                (self.__class__.__name__, self.name, self.job, self.pay))

class Manager(Person):
    """
    Inherits from Person and defaults to give a 10% bonus
    for the giveRaise function
    """
    def __init__(self, name, age, pay):
        """
        Initialize with the same constructor as the Person class but
        explicity choose 'manager' as the job title
        """
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus = 0.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager('Tom Doe', age = 50, pay = 50000)
    print(sue, sue.pay, sue.lastName())

    for obj in (bob, sue, tom):
        obj.giveRaise(0.10)
        print(obj)
