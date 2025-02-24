from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def register(self):
        pass

class Student(User):
    def login(self):
        print("logging in student")

    def register(self):
        print("registering student")

class Teacher(User):
    def login(self):
        print("logging in teacher")

    def register(self):
        print("registering teacher")

stu1 = Student()
stu1.login()
stu1.register()
teach1 = Teacher()
teach1.login()
teach1.register()