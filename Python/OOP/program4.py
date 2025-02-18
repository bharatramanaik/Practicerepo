class Employee:
    salary = 23

    @classmethod
    def printsalary(self):
        print(f"salary is class is {self.salary}")

    @property
    def name(self):
        return f"first name is {self.fname} last name is {self.lname}"

    @name.setter
    def name(self, val):
        self.fname = val.split(" ")[0]
        self.lname = val.split(" ")[1]
        

a = Employee()
a.salary = 87
a.printsalary()
a.name = "bharat naik"
print(a.name)