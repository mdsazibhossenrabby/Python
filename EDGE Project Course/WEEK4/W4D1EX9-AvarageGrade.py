

class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}")

    def AvarageGrade(self):
        return sum(self.grades)/len(self.grades)

stu=Student("Alice",20,[80,90,75])

stu.display()

print(f"The Avarage Grade : {stu.AvarageGrade()}")