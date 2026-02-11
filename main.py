from atm.atm_machine import ATM
from factory.account_factory import AccountFactory


def main():
    atm = ATM()

    # Create accounts
    acc1 = AccountFactory.create_account("savings", 101, "Rahul", 10000, 1234)
    acc2 = AccountFactory.create_account("current", 102, "Amit", 20000, 4321)

    atm.add_account(acc1)
    atm.add_account(acc2)

    acc_no = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    account = atm.authenticate(acc_no, pin)

    if account:
        atm.show_menu(account)
    else:
        print("Authentication failed!")


if __name__ == "__main__":
    main()
