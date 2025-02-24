class Student():
    numberOfStudents = 0 # class variable

    def __init__(self, name, rollno, age, marks):
        self.name = name
        self.age = age
        self._marks = marks     # protected member (can be accessed by child class and also outside the class)
        self.__rollno = rollno            
        Student.numberOfStudents += 1


    def __mymethod(self):
        print("this is private method")

    


s1 = Student("abc", 1, 12, 23)
s2 = Student("def", 2, 13, 45)
print(s1._marks)  
# print(s1.__mymethod())  #cannot be accessed
print(Student.numberOfStudents)