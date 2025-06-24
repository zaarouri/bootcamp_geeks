print("-" * 30)
print("Exercise 1 : Bank Account")

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Withdrawal must be positive")
        self.balance -= amount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required")
        if amount <= 0:
            raise Exception("Withdrawal must be positive")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot go below minimum balance")
        self.balance -= amount

class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("Invalid account list")
        if not isinstance(try_limit, int) or try_limit <= 0:
            try_limit = 2
        self.accounts = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")

    def log_in(self, username, password):
        for account in self.accounts:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return
        self.current_tries += 1
        print("Login failed.")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Goodbye.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                amount = int(input("Amount to deposit: "))
                try:
                    account.deposit(amount)
                    print(f"Balance: {account.balance}")
                except Exception as e:
                    print(e)
            elif choice == "2":
                amount = int(input("Amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print(f"Balance: {account.balance}")
                except Exception as e:
                    print(e)
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
# Define the accounts
acc1 = BankAccount("alice", "1234")
acc2 = MinimumBalanceAccount("bob", "abcd", minimum_balance=100)

# Preload balances for testing
acc1.authenticated = True
acc1.deposit(500)
acc1.authenticated = False

acc2.authenticated = True
acc2.deposit(300)
acc2.authenticated = False

# Create ATM with both accounts
atm = ATM([acc1, acc2], try_limit=3)