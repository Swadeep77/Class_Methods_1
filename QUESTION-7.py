"""Create a class Employee with:
	instance attributes: name, base_salary
	class variable: bonus_rate = 0.1
	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
	class method: update_bonus(cls, new_rate) → updates bonus for all employees
	static method: is_valid_salary(sal) → checks if salary > 0
Create two employees, show final salaries, update bonus rate, and show again."""

class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        final_sal=self.base_salary+(self.base_salary*Employee.bonus_rate)
        return final_sal
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return "Valid"
        return "Not Valid"

Emp1=Employee("Swadeep",50000)
Emp2=Employee("Deekshith",30000)
print(Emp1.final_salary())
print(Emp2.final_salary())
Employee.update_bonus(0.3)
print(Emp1.final_salary())
print(Emp2.final_salary())


