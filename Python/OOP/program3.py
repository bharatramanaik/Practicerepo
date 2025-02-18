class Employee:
    a = 2

class Coder(Employee):
    b = 4

class Programmer(Coder):  # multiple inheritence
    c = 5

a = Programmer()
print()
