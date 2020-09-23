# python Object oriented programming

class Employee:
    class_var = 105
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        print(f'{self.first} {self.last}')



e_1 = Employee('corey','scha',12)


print(e_1.__dict__)
