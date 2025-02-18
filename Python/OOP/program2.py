class Employee:
    name = "abc"
    company = "jkl"
    def showdetails(self):
        print(f"name is {self.name} and company is {self.company}")

class Coder:
    language = "python"
    def printlanguages(self):
        print(f"language is {self.language}")

class Programmer(Employee, Coder):  # multiple inheritence
    def showalldetails(self):
        print("hi")

a = Programmer()
a.showdetails()
a.printlanguages()
a.showalldetails()