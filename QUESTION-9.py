""""Create a class BankAccount with:
	class variable bank_name
	instance variables holder and balance
	instance method deposit(amount)
	class method change_bank_name(cls, new_name)
	static method validate_amount(amount) → returns True if amount > 0
Show transactions and how static + class methods work together."""""

class BankAccount:
    bank_name = "State Bank of India"
    def __init__(self, holder, balance):

        self.holder = holder
        self.balance = balance
        self.amount = None
    def deposit(self, amount):
        self.amount = amount
        final_amount = self.balance + self.amount
        return final_amount
    @classmethod
    def change_bank_name(cls, new_name):
        BankAccount.bank_name = new_name
    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        return False
Acc1 = BankAccount("Swadeep", 100000)
Acc2 = BankAccount("Deekshith", 50000)
Acc3 = BankAccount("Yash", 25000)
print(Acc1.deposit(30000))
print(Acc2.deposit(30000))
print(Acc3.deposit(30000))