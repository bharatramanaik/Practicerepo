# multilevel inheritence
class Employee:
    def __init__(self):
        print("construtor of employee")
    a = 2

class Coder(Employee):
    def __init__(self):
        super().__init__()
        print("construtor of coder")
    b = 4

class Programmer(Coder):
    def __init__(self):
        super().__init__()
        print("construtor of programmer") 
    c = 5

obj = Programmer()
print(obj.a,obj.b, obj.c)
