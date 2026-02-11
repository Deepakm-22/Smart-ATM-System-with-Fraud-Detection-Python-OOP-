from accounts.savings import SavingsAccount
from accounts.current import CurrentAccount


class AccountFactory:
    @staticmethod
    def create_account(acc_type, acc_no, name, balance, pin):
        if acc_type == "savings":
            return SavingsAccount(acc_no, name, balance, pin)
        elif acc_type == "current":
            return CurrentAccount(acc_no, name, balance, pin)
        else:
            raise ValueError("Invalid account type")
