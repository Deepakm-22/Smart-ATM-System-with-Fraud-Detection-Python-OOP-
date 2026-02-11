from .account import Account
class CurrentAccount(Account):
    def withdraw(self, amount):
        # Overdraft allowed (basic example)
        super().withdraw(amount)
