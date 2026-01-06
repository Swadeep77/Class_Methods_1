class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks > 40:
            return True
        return False
std1=Student("Swadeep",75)
std2=Student("Deekshith",35)
print(std1.is_passed())
print(std2.is_passed())