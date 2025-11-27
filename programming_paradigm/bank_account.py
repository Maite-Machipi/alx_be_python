# bank_account.py

import sys

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount < 0:
            return
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the amount if sufficient funds exist."""
        if amount < 0:
            return False

        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance:2f}")

