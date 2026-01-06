"""Create a class Temperature with:
	instance attribute celsius
	a static method to_fahrenheit(celsius)
	an instance method show_conversion() that uses the static method to print both values"""

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenhiet(celsius):
        f = (celsius*9/5)+32
        return f
    def show_conversion(self):
        f = (self.celsius*9/5)+32
        return self.celsius, f
Temp1 = Temperature(38)
print(Temp1.show_conversion())
print(Temperature.to_fahrenhiet(35))
