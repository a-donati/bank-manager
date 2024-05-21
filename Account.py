class Account:
    """
    Initializes the Account class

    Takes in first, last, social security number, and pin from the user
    the account ID is initially set to none but generated through the BankUtility.generateRandomInteger() 
    """

    def __init__(self, first_name, last_name, ssid, pin, account_id=None, initial_balance=0):
        # Account attributes
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.ssid = ssid
        self.pin = pin
        self.balance = initial_balance
    # Getters and setters for attributes

    def set_first_name(self, ownerFirstName):
        self.first_name = ownerFirstName

    def get_first_name(self):
        return self.first_name

    def setPIN(self, new_pin):
        self.pin = new_pin
        return self.pin

    def display(self):
        print(f"""

                    ============================================================
                    Account Number: {self.account_id}
                    Owner First Name: {self.first_name}
                    Owner Last Name: {self.last_name}
                    Owner SSN: {self.ssid}
                    PIN: {self.pin}
                    Balance: {self.balance/100:.2f}
                    ============================================================""")

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            return self.balance

    def getBalance(self):
        return self.balance

    def getAccountNumber(self):
        return self.account_id

    def isValidPIN(self, pin):
        if self.pin == pin:
            return True
        else:
            return False
