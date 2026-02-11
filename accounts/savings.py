from .account import Account


class SavingsAccount(Account):
    MIN_BALANCE = 500

    def withdraw(self, amount):
        if self.get_balance() - amount < self.MIN_BALANCE:
            print("Minimum balance rule violated!")
        else:
            super().withdraw(amount)
