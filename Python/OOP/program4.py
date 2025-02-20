class Employee:
    salary = 23
    __role = "dev"  # this is private(when 2 underscores are added before variable name it becomes private)

    @classmethod
    def printsalary(self):
        print(f"salary is {self.salary}")

    @property
    def name(self):
        return f"first name is {self.fname} last name is {self.lname}"

    @name.setter
    def name(self, val):
        self.fname = val.split(" ")[0]
        self.lname = val.split(" ")[1]
        
    def get_role(self):
        return self.__role
    
    def set_role(self, role):
        self.__role = role
    

a = Employee()
print(isinstance(a, Employee))
a.salary = 87
a.printsalary()
a.name = "bharat naik"
a.set_role("devops")
print(a.name)
print("role is ",a.get_role())
