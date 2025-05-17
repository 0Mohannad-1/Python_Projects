while True:
    owner = input("What Is The Owner's Name: ").strip().capitalize()
    if owner.isalpha():
        break
    else:
        print("Please Enter A Valid Name Using Letters Only.")

while True:
    try:
        balance = float(input("What Is The Owner's Balance: "))
        break
    except ValueError:
        print("Please Enter A Valid Number For The Balance.")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Must Be Greater Than Zero.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal Amount Must Be Greater Than Zero.")
            return
        elif amount > self.balance:
            print("Insufficient Funds.")
            return
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Owner: {self.owner}, Balance: ${self.balance:.2f}")

account = BankAccount(owner, balance)

while True:
    operation = input("\nDeposit, Withdraw, Or Quit? ").capitalize().strip()

    if operation == "Deposit":
        try:
            amount = float(input("Enter Amount To Deposit: "))
            account.deposit(amount)
            account.display_balance()
        except ValueError:
            print("Please Enter A Valid Number.")

    elif operation == "Withdraw":
        try:
            amount = float(input("Enter Amount To Withdraw: "))
            account.withdraw(amount)
            account.display_balance()
        except ValueError:
            print("Please Enter A Valid Number.")

    elif operation == "Quit":
        print("Thank You For Using The Banking App. Goodbye!")
        break

    else:
        print("Invalid Operation. Please Enter Deposit, Withdraw, Or Quit.")
