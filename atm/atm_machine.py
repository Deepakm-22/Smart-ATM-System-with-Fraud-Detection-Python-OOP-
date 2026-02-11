class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def authenticate(self, acc_no, pin):
        account = self.accounts.get(acc_no)
        if account and account.verify_pin(pin):
            return account
        return None

    def show_menu(self, account):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Transactions\n5. Exit")
            choice = input("Choose option: ")

            if choice == "1":
                amt = float(input("Amount: "))
                account.deposit(amt)

            elif choice == "2":
                amt = float(input("Amount: "))
                account.withdraw(amt)

            elif choice == "3":
                print("Balance:", account.get_balance())

            elif choice == "4":
                account.show_transactions()

            elif choice == "5":
                break
