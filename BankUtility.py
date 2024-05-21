import random

class BankUtility:

    def __init(self):
        pass

    def promptUserForString(prompt):
        """
        Prompt response from user
        Returns either user_input
        or None if the user types 'return'
        """
        # Print the prompt
        print(prompt)
        # Read input from the user and return it as a string
        user_input = input()
        # Check if the user entered "return"
        if user_input.upper() == "RETURN":
            # Return None to indicate that the user wants to go back
            return None
        # Return the valid user input as a string
        return user_input

    def promptUserForPositiveNumber(prompt):
        """
        Takes prompt values from the user, a string
        String will be converted to a float
        Once the conditions are validated, this returns
        a positive number
        """
        # Create a loop to keep prompting the user for a valid input
        while True:
            user_input = input(prompt)
            try:
                user_input = float(user_input)
                if user_input <= 0:
                    print(
                        "Invalid Number. Amount cannot be negative or zero. Please try again.")
                else:
                    return user_input
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def generateRandomInteger():
        # Removed params to use this to generate social security and account numbers
        # rand_int = random.randint(min, max)
        id_number = random.randint(10000000, 99999999)
        return id_number

    """
    Converts dollars into a long cent format to be added or 
    subtracted to the account's total balance
    Returns cents
    """
    def convertFromDollarsToCents(dollars_str):
        try:
            # Convert the input string to a float
            dollars = float(dollars_str)
            # Multiply the dollar amount by 100 and round to the nearest integer
            cents = round(dollars * 100)
            return cents
        except ValueError:
            # Handle the case where the input is not a valid float
            print("Invalid input. Please enter a valid dollar amount.")
            return None

    """
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     """
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isnumeric():
                return True
            else:
                return False
        except ValueError:
            return False
