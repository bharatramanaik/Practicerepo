class Employee:
    role = "dev" # class attribute
    salary = 1000

    def __init__(self, role, salary):  # acts as constructor
        self.role = role
        self.salary = salary
        print("this is dundle method which is automatocaly called")

    def getSalary(self):
        print(f"Salary is: {self.salary}")

    @staticmethod
    def greet():
        print("hi")

obj = Employee("devops", 123)
# obj.salary = 200
obj.name = "bharat"  #instance attribute
print(obj.name)
obj.getSalary()
Employee.greet()