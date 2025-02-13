class Employee:
    role = "dev"
    salary = 1000

    def getSalary(self):
        print(f"Salary is: {self.salary}")

bharat = Employee()
bharat.salary = 200
bharat.getSalary()