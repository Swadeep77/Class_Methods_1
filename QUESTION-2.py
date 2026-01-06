"""Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances."""

class Employee:
    company_name = "TechCorp"
    def __init__(self,name):
        self.name = name
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
Emp1=Employee("Swadeep")
Emp2=Employee("Deeksh")
print(Emp1.name,Emp1.company_name)
print(Emp2.name,Emp2.company_name)
Employee.change_company("SoftTech")
print(Emp1.name,Emp1.company_name)
print(Emp2.name,Emp2.company_name)