"""
Project: Simple Banking System
------------------------------
Demonstrates OOP concepts — Encapsulation, Inheritance, and Modular Design.
Includes a base Account class and derived SavingsAccount and CurrentAccount classes.

Time Complexity: O(1) for deposit, withdraw, and balance check
Space Complexity: O(1)
"""

class Account:
    """Base class representing a bank account."""
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number   # Encapsulated attribute
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    """Derived class representing a savings account with interest."""
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ₹{interest}")


class CurrentAccount(Account):
    """Derived class representing a current account with overdraft limit."""
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=10000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Overdraft limit exceeded.")


# Example usage
if __name__ == "__main__":
    acc1 = SavingsAccount("SB1001", "Aarav Sharma", 5000)
    acc1.deposit(2000)
    acc1.add_interest()

    acc2 = CurrentAccount("CA2001", "Neha Gupta", 10000)
    acc2.withdraw(15000)
