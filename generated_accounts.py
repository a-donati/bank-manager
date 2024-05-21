from Account import Account
from BankUtility import BankUtility

# Generate test accounts
test_accounts_list = []
for i in range(1, 21):
    # Generate some sample account details
    first_name = f"First{i}"
    last_name = f"Last{i}"
    ssn = BankUtility.generateRandomInteger()
    pin = "1234"  # Assuming a default PIN
    # Appending 'i' as the last account number for simplicity
    account_number = BankUtility.generateRandomInteger()
    # Create an Account object and append it to the list
    initial_balance = 500
    test_account = Account(first_name, last_name, ssn,
                           pin, account_number, initial_balance)
    test_accounts_list.append(test_account)

# Now you can pass this list of test accounts to the Bank class
