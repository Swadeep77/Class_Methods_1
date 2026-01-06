"""Create a class Course with:
	class variable total_students
	instance variable student_name
	instance method enroll() → increments total_students
	class method show_total(cls) → prints total students
	static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count. """

class Course:
    total_students = 0
    def __init__(self, student_name):
        self.student_name = student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        return cls.total_students
    @staticmethod
    def is_elgible(age):
        if age >= 18:
            return True
        return False
Std1 = Course("Swadeep")
Std1.enroll()
print(Course.total_students)
Std2 = Course("Deekshith")
Std3 = Course("Yash")
Std2.enroll()
Std3.enroll()
print(Course.total_students)