from Account import Account

class Bank:
    def __init__(self, accounts):
        # Create an array to store Account objects
        self.accounts = accounts

    def print_accounts(self):
        # Display total account information in the array
        for account in self.accounts:
            print(account.display())

    def addAccountToBank(self, account):
        # Set limit on the amount of accounts available
        if len(self.accounts) < 100:
            self.accounts.append(account)
            print("Account Opened")
            print("New Account Number:", account.getAccountNumber())
            return True
        else:
            print("No more accounts available")
            return False

    def addTestAccountsToBank(self, testing_accounts_list):
        # Add test accountd array to self.accounts
        for test_acc in testing_accounts_list:
            self.accounts.append(test_acc)

    def removeAccountFromBank(self, account):
        # Check if account exists, then remove it
        if account in self.accounts:
            self.accounts.remove(account)
            print("Account removed")
            return True
        else:
            print("Account not found")
            return False

    def findAccount(self, accountNumber):
        # Iterate through accounts and find the one with the matching account number
        for account in self.accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        # If no matching account is found, return None
        return None

    def addMonthlyInterest(self, percent):
        # Iterate through all accounts and add monthly interest
        for account in self.accounts:
            # Calculate interest based on current balance and provided percentage
            # Convert annual interest rate to monthly
            monthly_interest = (percent / 12) / 100
            interest_amount = int(account.getBalance() * monthly_interest)
            # Deposit the interest amount into the account
            account.deposit(interest_amount)
