import unittest
from BankUtility import BankUtility
from CoinCollector import CoinCollector
from Account import Account

class TestBankUtility(unittest.TestCase):

    def test_parseChange_valid_input(self):
        # Test parsing valid input
        coins = "PPNNDDQQHHWW"
        parsed_coins = CoinCollector.parseChange(coins)
        self.assertEqual(parsed_coins, 382)

    def test_parseChange_invalid_input(self):
        # Test parsing invalid input
        coins = "XYZ"
        parsed_coins = CoinCollector.parseChange(coins)
        self.assertEqual(parsed_coins, 0)

    def test_deposit(self):
        # Test depositing money into the account
        initial_balance = 1000
        deposit_amount = 500
        account = Account("John", "Doe", "123456789",
                          "1234", 1, initial_balance)
        account.deposit(deposit_amount)
        self.assertEqual(account.getBalance(),
                         initial_balance + deposit_amount)

    def test_withdraw_sufficient_funds(self):
        # Test withdrawing with sufficient funds
        initial_balance = 1000
        withdrawal_amount = 500
        account = Account("John", "Doe", "123456789",
                          "1234", 1, initial_balance)
        account.withdraw(withdrawal_amount)
        self.assertEqual(account.getBalance(),
                         initial_balance - withdrawal_amount)

    def test_withdraw_insufficient_funds(self):
        # Test withdrawing with insufficient funds
        account = Account("John", "Doe", "123456789", "1234", 1)
        account.withdraw(150)
        # Balance should remain unchanged
        self.assertEqual(account.getBalance(), 0)

    def test_isValidPIN_valid(self):
        # Test validating a valid PIN
        account = Account("John", "Doe", "123456789", "1234", 1)
        pin = "1234"
        self.assertTrue(account.isValidPIN(pin))

    def test_isValidPIN_invalid(self):
        account = Account("John", "Doe", "123456789", "1234")
        # Test validating an invalid PIN
        pin = "9999"
        self.assertFalse(account.isValidPIN(pin))

    def test_generateRandomInteger(self):
        # Test generating a random integer
        random_int = BankUtility.generateRandomInteger()
        self.assertIsInstance(random_int, int)


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
