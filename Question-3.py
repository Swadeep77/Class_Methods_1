"""Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance."""

class MathOps:
    def __init__(self,number):
        self.number = number
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        return False
Math1=MathOps(24)
Math2=MathOps(27)
print(MathOps.is_even(Math1.number))
print(MathOps.is_even(Math2.number))
