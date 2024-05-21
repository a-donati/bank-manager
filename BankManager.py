from BankUtility import BankUtility
from Bank import Bank
from Account import Account
from CoinCollector import CoinCollector
from generated_accounts import test_accounts_list

class BankManager:
    """
    BankManager class manages the operations related to the bank such as opening accounts, managing account information,
    transferring money, withdrawing money, etc.
    """

    def __init__(self):
        """
        Initializes a new instance of the BankManager class.
        """
        self.bank = Bank([])
        # Add test accounts
        self.bank.addTestAccountsToBank(test_accounts_list)

    def promptForAccountNumberandPIN(self):
        """
        Prompts the user for an account number and PIN, validates the input, and returns the corresponding account if valid.

        Returns:
            Account: The account corresponding to the entered account number and PIN if valid, otherwise None.
        """
        while True:
            account_number = BankUtility.promptUserForString(
                "Enter account number: ")
            if account_number is None:
                print("Returning To Main Menu")
                return None
            elif not account_number.isdigit():
                print("Please enter a valid account number")
                # Prompt again if input is not valid
                continue
            else:
                try:
                    # Pass info to findAccount method
                    account = self.bank.findAccount(int(account_number))
                    # Check if account is found
                    if not account:
                        print(f"Account not found for account number: {account_number}")
                        # Prompt again if account is not found
                        continue
                    pin = BankUtility.promptUserForString("Enter PIN: ")
                    if pin is None:
                        print("Returning To Main Menu")
                        return None
                    elif not account.isValidPIN(pin):
                        print("Invalid PIN")
                        # Prompt again if PIN is invalid
                        continue
                    # Once validated, return account object
                    return account
                except:
                    print("Error has occurred")
                    # Prompt again if an error occurs
                    continue

    def transferPromptForAccountNumberandPIN(self):
        """
        Prompts the user for source and destination account numbers and PINs, validates the input, and returns 
        corresponding accounts if valid.

        Returns:
            tuple: A tuple containing the source and destination accounts if inputs are valid, otherwise None.
        """
        while True:
            # Prompt for the source account number and PIN
            from_account_number = BankUtility.promptUserForString(
                "Enter account number to withdraw from: ")
            if from_account_number is None:
                print("Returning To Main Menu")
                return None
            elif from_account_number.isnumeric() == False:
                print("Please enter a valid account number")
                # Prompt again if input is not valid
                continue
            else:
                try:
                    # Pass info to findAccount method
                    from_account = self.bank.findAccount(
                        int(from_account_number))
                    if not from_account:
                        print(f"Account not found for account number: {from_account_number}")
                        # Prompt again if account is not found
                        continue
                    else:
                        from_pin = BankUtility.promptUserForString(
                            "Enter PIN for source account: ")
                        if from_pin is None:
                            print("Returning to Main Menu")
                            return None
                        elif not from_account.isValidPIN(from_pin):
                            print("Invalid PIN entered for source account")
                            # Prompt again if PIN is invalid
                            continue
                except:
                    print("An error has occurred")
                    # Prompt again if an error occurs
                    continue

            # Prompt for the destination account number
            to_account_number = BankUtility.promptUserForString(
                "Enter account number to transfer to: ")
            if to_account_number is None:
                print("Returning To Main Menu")
                return None
            elif to_account_number.isnumeric() == False:
                print("Please enter a valid account number")
                # Prompt again if input is not valid
                continue
            else:
                try:
                    to_account = self.bank.findAccount(int(to_account_number))
                    if not to_account:
                        print(f"Destination account not found for account number: {to_account_number}")
                        # Prompt again if account is not found
                        continue
                    else:
                        to_pin = BankUtility.promptUserForString(
                            "Enter PIN for destination account: ")
                        if to_pin is None:
                            print("Returning to Main Menu")
                            return None
                        elif not to_account.isValidPIN(to_pin):
                            print("Invalid PIN for destination account")
                            # Prompt again if PIN is invalid
                            continue
                    # Return both accounts
                    return from_account, to_account
                except:
                    print("An error has occurred")
                    # Prompt again if an error occurs
                    continue

    def openAccount(self):
        """
        Opens a new bank account using the user-supplied information.
        """
        print("\nOpen An Account")
        while True:
            first_name = BankUtility.promptUserForString("Enter First Name: ")
            if first_name == None:
                print("Returning To Main Menu")
                return
            elif len(first_name) > 50:
                # Prompt user again if input is invalid
                print("First name is too long. Please enter a shorter name.")
                continue
            else:
                # Break out of the loop if input is valid
                break
        while True:
            last_name = BankUtility.promptUserForString("Enter Last Name: ")
            if last_name == None:
                print("Returning To Main Menu")
                return
            elif len(last_name) > 50:
                print("Last name is too long. Please enter a shorter name.")
                continue
            else:
                # Break out of the loop if input is valid
                break
        while True:
            ssn = BankUtility.promptUserForString(
                "Enter Social Security Number: ")
            if ssn == None:
                print("Returning To Main Menu")
                return
            elif not ssn.isnumeric():
                print("Invalid Social Security Number. Only Numeric Values Are Allowed")
            elif len(ssn) != 9:
                print("Invalid Social Security Number. Please enter exactly 9 digits.")
                # Prompt user again if input is invalid
                continue
            else:
                # Break out of the loop if input is valid
                break
        while True:
            pin = BankUtility.promptUserForString("Enter a Four Digit Pin: ")
            if pin == None:
                print("Returning To Main Menu")
                return
            elif not pin.isnumeric():
                print("Invalid PIN Number. Only Numeric Values Are Allowed")
                # continue
            elif len(pin) != 4:
                print("Invalid PIN. Please enter exactly 4 digits.")
                # Prompt user again if input is invalid
                continue
            else:
                # Break out of the loop if input is valid
                break
        # Generate account number
        account_number = BankUtility.generateRandomInteger()
        # Check if account number already exists
        if self.bank.findAccount(account_number):
            # if so, generate another number
            account_number = BankUtility.generateRandomInteger()
        else:
            new_account = Account(first_name, last_name,
                                  ssn, pin, account_number)
            self.bank.addAccountToBank(new_account)

    def getAccountInfoAndBalance(self):
        """
        Displays the account information and balance for a given account.
        """
        print("Get Account Informartion And Balance")
        account = self.promptForAccountNumberandPIN()
        if account:
            account.display()

    def changePIN(self):
        """
        Changes the PIN for a given account.
        """
        print("Change PIN")
        account = self.promptForAccountNumberandPIN()
        # If the account exists, update the pin
        if account:
            while True:
                new_pin = BankUtility.promptUserForString("Enter new PIN: ")
                if new_pin is None:
                    print("Returning To Main Menu")
                    return
                if len(new_pin) != 4:
                    print("PIN must be 4 digits")
                    continue  # Prompt again if PIN length is not 4
                confirm_pin = BankUtility.promptUserForString(
                    "Enter new PIN again to confirm: ")
                # Validate that the desired PIN and confirmation PIN match
                if confirm_pin is None:
                    print("Returning To Main Menu")
                    return
                elif new_pin != confirm_pin:
                    print("The entered PINs do not match, try again.")
                    # Prompt again if PINs don't match
                    continue
                else:
                    account.setPIN(new_pin)
                    print("PIN updated")
                    # Exit the loop if PIN is successfully updated
                    break

    def depositMoney(self):
        """
        Deposits money into a given account.
        """
        account = self.promptForAccountNumberandPIN()
        if account:
            amount = BankUtility.promptUserForPositiveNumber(
                "Enter amount to deposit in dollars and cents (e.g. 2.57): ")
            conversion_amount = BankUtility.convertFromDollarsToCents(amount)
            account.deposit(conversion_amount)
            # Display amount to user
            print(f"New balance: ${account.getBalance()/100:.2f}")

    def transferMoney(self):
        """
        Transfers money between two accounts.
        """
        print("Transfer Money Between Accounts")
        # Validate account credentials
        accounts = self.transferPromptForAccountNumberandPIN()
        if accounts:
            from_account, to_account = accounts
            amount = BankUtility.promptUserForPositiveNumber(
                "Enter the amount of money to transfer in dollars and cents (e.g. 2.57): ")
            # Ensure that the amount is greater than zero and also exists in the account
            conversion_amount = BankUtility.convertFromDollarsToCents(amount)

            if conversion_amount > 0 and from_account.getBalance() >= conversion_amount:
                from_account.withdraw(conversion_amount)
                to_account.deposit(conversion_amount)
                print("Transfer Complete")
                print(f"New balance in source account: {from_account.getAccountNumber()} is ${from_account.getBalance()/100:.2f}")
                print(f"New balance in destination account: {to_account.getAccountNumber()} is ${to_account.getBalance()/100:.2f}")
            else:
                print(f"Insufficient funds in account {from_account.getAccountNumber()}")

    def withdrawMoney(self):
        """
        Withdraws money from a given account.
        """
        print("Withdraw Money From Account")
        account = self.promptForAccountNumberandPIN()
        if account:
            available_balance = account.getBalance()  # Convert balance to dollars
            amount = BankUtility.promptUserForPositiveNumber(
                "Enter the amount of money to withdraw in dollars and cents (e.g. 2.57): ")
            conversion_amount = BankUtility.convertFromDollarsToCents(amount)

            # Ensure that funds exist in account
            if available_balance < conversion_amount:
                print(f"Insufficient funds in account {account.getAccountNumber()}")
            else:
                # conversion_amount = BankUtility.convertFromDollarsToCents(amount)
                account.withdraw(conversion_amount)
                print(f"New balance: ${account.getBalance()/100:.2f}")

    def atmWithdrawal(self):
        """
        Simulates an ATM withdrawal from a given account.
        """

        account = self.promptForAccountNumberandPIN()
        if account:
            available_balance = account.getBalance() / 100  # Convert balance to dollars

            while True:
                amount = BankUtility.promptUserForPositiveNumber(
                    "Enter the amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): ")
                # Check that amount is a multiple of 5
                if amount % 5 != 0 or amount < 5 or amount > 1000:
                    print(
                        "Invalid amount, the amount must be withdrawn in dollars (no cents) in multiples of $5 (limit $1000)")
                elif available_balance < amount:
                    print(f"Insufficient funds in account {account.getAccountNumber()}")
                elif available_balance < amount:
                    print(f"Insufficient funds in account {account.getAccountNumber()}")
                else:
                    # Withdraw the amount in cents
                    amount_in_cents = int(amount * 100)
                    account.withdraw(amount_in_cents)
                    # Display the denominations of bills
                    num_twenty = amount // 20
                    amount -= num_twenty * 20
                    num_ten = amount // 10
                    amount -= num_ten * 10
                    num_five = amount // 5
                    print(f"Number of 20-dollar bills: {num_twenty}")
                    print(f"Number of 10-dollar bills: {num_ten}")
                    print(f"Number of 5-dollar bills: {num_five}")
                    print(f"New balance: ${account.getBalance()/100:.2f}")
                    break  # Exit the loop after successful withdrawal

    def depositChange(self):
        """
        Deposits coins into a given account.
        Amounts to enter:
                ‘P’ represents a penny (1 cent)
                ‘N’ represents a nickel (5 cents)
                ‘D’ represents a dime (10 cents)
                ‘Q’ represents a quarter (25 cents)
                ‘H’ represents a half-dollar (50 cents)
                ‘W’ represents a whole dollar (100 cents)
        """
        account = self.promptForAccountNumberandPIN()
        if account:
            print("""
                Amounts to enter:
                ‘P’ represents a penny (1 cent)
                ‘N’ represents a nickel (5 cents)
                ‘D’ represents a dime (10 cents)
                ‘Q’ represents a quarter (25 cents)
                ‘H’ represents a half-dollar (50 cents)
                ‘W’ represents a whole dollar (100 cents)
                """)
            coins = BankUtility.promptUserForString("Deposit coins: ")
            if coins == None:
                print("Returning To Main Menu")
                return
            # Parse change into a long
            coin_value = CoinCollector.parseChange(coins)
            if coin_value != None:
                # Store long value
                account.deposit(coin_value)
                # Display the total amount of coins value to the user and the new balance
                print(f"${coin_value/100:.2f} in coins deposited into account")
                print(f"New balance: ${account.getBalance()/100:.2f}")

    def closeAccount(self):
        """
        Closes a given account.
        """
        account = self.promptForAccountNumberandPIN()
        if account:
            self.bank.removeAccountFromBank(account)
            print(f"Account {account.getAccountNumber()} closed")

    # def generateInterest(self):
    #     user_interest = BankUtility.promptUserForPositiveNumber("Enter annual interest rate percentage (e.g. 2.75 for 2.75%): ")
    #     self.bank.addMonthlyInterest(user_interest)

    def main(self):
        """
        Main menu function that prompts the user for input and executes corresponding operations based on the input.
        """
        # Initiate while loop to keep prompting the user for input after finished selections
        while True:
            """Enter a choice from 1 to 10. Type 'Return' in order to return to the main menu and break out of the loop
            """
            print("""
                ============================================================
                What do you want to do? 
                        1. Open an account
                        2. Get account information and balance
                        3. Change PIN
                        4. Deposit money in account
                        5. Transfer money between accounts
                        6. Withdraw money from account
                        7. ATM withdrawal
                        8. Deposit change
                        9. Close an account
                        10. End Program
                ============================================================ """)
            choice = BankUtility.promptUserForString("Enter your choice: ")
            print()
            """Option 12 is available for developmental testing purposes only and would not be visible to the user during production, entering 12 as a choice will display all account information and details to the console
            """
            if choice == '1':
                self.openAccount()
            elif choice == '2':
                self.getAccountInfoAndBalance()
            elif choice == '3':
                self.changePIN()
            elif choice == '4':
                self.depositMoney()
            elif choice == '5':
                self.transferMoney()
            elif choice == '6':
                self.withdrawMoney()
            elif choice == '7':
                self.atmWithdrawal()
            elif choice == '8':
                self.depositChange()
            elif choice == '9':
                self.closeAccount()
            # elif choice == '10':
            #     self.generateInterest()
            elif choice == '10':
                print("Exiting Program")
                break
            elif choice == '12':
                print("Printing All Account Information")
                self.bank.print_accounts()
            else:
                print("Invalid choice, please enter a valid option.")


# Starting the program
if __name__ == "__main__":
    bank_manager = BankManager()
    bank_manager.main()
