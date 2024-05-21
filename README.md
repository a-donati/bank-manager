## Bank Management System

# Overview
The Bank Management System is a Python program designed to manage various banking operations such as opening accounts, depositing and withdrawing money, transferring funds between accounts, changing PINs, and more. It provides a user-friendly interface for customers to interact with their accounts and perform necessary transactions. The account information is stored in an array, this was a specification from the project guidelines. In the future I would like to add database functionality.
- generated_accounts.py contains test account information

# Features
Account Management: Users can open new accounts, view account information, and close accounts.
Transaction Operations: Deposit and withdraw money, transfer funds between accounts, and perform ATM withdrawals.
Security: Change PINs for accounts to ensure security and privacy.
Coin Deposits: Allow users to deposit coins into their accounts.

# Usage
- Run the program by executing the BankManager.py file.
- Depending on the user's operating system/terminal setup, the program can be run using these commands in the computer terminal or IDE terminal:
`python deque.py`
or
`python3 deque.py` 

- To run unit testing use command:
`python -m unittest`
or
`python3 -m unittest`

- Program will list 10 options for the user to choose from
- Enter a number to select the desired option:
    - Add items to the beignning and end of the queue
    - Remove items from the beginning or end of the queue 
    - Print the queue 

- Upon running the program, you will be presented with a menu of options.
    - Choose an option by entering the corresponding number.
    - Follow the prompts to perform the desired operation (e.g., open an account, deposit money, etc.)
    - Repeat steps 2-3 as needed to navigate through the program and perform various banking operations.
    - ype "Return" in order to return to the main menu
    - To exit the program, select the "End Program" option from the menu by entering "10".


# Algorithm Overview
1. Initialization:
    - The program initializes a BankManager object, which manages the bank operations.
    - It loads test accounts into the bank from a predefined list.
2. Main Menu:
    - The program enters a loop to display the main menu and prompt the user for their choice.
    - The user can choose from various banking operations like opening an account, checking balance, transferring money, etc.
3. User Input and Validation:
    - For operations requiring user input, the program prompts the user and validates the input according to predefined rules.
    - Inputs such as account numbers, PINs, amounts, etc., are checked for validity.
4. Bank Operations:
    - Based on the user's choice, the program executes the corresponding bank operation.
    - This includes actions like opening an account, checking balance, depositing money, withdrawing money, transferring money, changing PINs, etc.
    - Each operation involves interaction with the bank's Account objects, performing necessary calculations and updates.
5. Account Management:
    - Account-related operations involve retrieving account details, updating balances, changing PINs, etc.
6. Error Handling:
    - Handle errors by displaying informative messages to the user.
    - Errors can occur due to invalid inputs, insufficient funds, account not found, etc.
    - Users are prompted to re-enter valid inputs or take appropriate actions.
7. Termination:
    - The program provides an option to exit when the user is done with their banking tasks.
    - Upon choosing the exit option, the program terminates.