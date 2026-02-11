from transactions.transaction import Transaction

class Account:
    def __init__(self, acc_no, name, balance, pin):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance     
        self.__pin = pin            
        self.is_frozen = False
        self.failed_attempts = 0
        self.transactions = []

    def verify_pin(self, pin):
        if self.is_frozen:
            print("Account is frozen!")
            return False

        if pin == self.__pin:
            self.failed_attempts = 0
            return True
        else:
            self.failed_attempts += 1
            print("Wrong PIN!")

            if self.failed_attempts >= 3:
                self.freeze_account()

            return False

    def deposit(self, amount):
        if self.is_frozen:
            print("Account frozen!")
            return

        self.__balance += amount
        self.add_transaction("Deposit", amount)
        print("Deposit successful")

    def withdraw(self, amount):
        if self.is_frozen:
            print("Account frozen!")
            return

        if amount > 50000:
            print("Suspicious transaction detected!")
            self.freeze_account()
            return

        if amount <= self.__balance:
            self.__balance -= amount
            self.add_transaction("Withdraw", amount)
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def freeze_account(self):
        self.is_frozen = True
        print("Account has been FROZEN!")

    def unfreeze_account(self):
        self.is_frozen = False
        self.failed_attempts = 0
        print("Account unfrozen")

    def add_transaction(self, t_type, amount):
        transaction = Transaction(t_type, amount)
        self.transactions.append(transaction)

    def show_transactions(self):
        for t in self.transactions:
            print(t)
