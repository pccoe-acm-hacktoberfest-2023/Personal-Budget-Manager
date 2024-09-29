# Personal-Budget-Manager
Key Features:
1.Expense Management:
    -You can add expenses to specific categories, ensuring the total amount spent is tracked.
    -It prevents negative expense values from being added.
2.Budget Tracking:
    -It maintains the total budget and calculates how much of it is left after expenses are made.
    -It can warn the user if they have exceeded the budget.
3.File Persistence:
    -The expenses and budget details can be saved to a file and reloaded later for persistence between sessions.
4.Resetting Expenses:
    -All expenses can be reset, clearing both the tracked spending and the category details.

    
Pre-requisites are needed
1. Basic Python Knowledge
    -Variables and Data Types: Understanding of Python's basic data types (integers, strings, lists, dictionaries, etc.).
    -Control Flow: Familiarity with conditionals (if, else), loops (for, while), and exception handling (try-except).
    -Functions: Ability to define and use functions for modular programming.
    -Classes and Objects: Understanding of object-oriented programming (OOP) to work with classes, methods, and attributes.
2. Python Setup
    -Python 3.x: Ensure Python 3.x is installed. You can download it from the official Python website.
    -Text Editor or IDE: Use an editor like VS Code, PyCharm, Sublime Text, or even Python’s built-in IDLE to write and run the code.
3. File Handling in Python
    -Knowledge of reading from and writing to files (using open(), read(), write() methods).
    -Understanding how to handle potential file errors (e.g., file not found) using exception handling.
4. Object-Oriented Programming (OOP)
    -Classes and Objects: Know how to define classes, and instantiate objects (like BudgetManager).
    -Methods: Be able to define and use methods inside a class.
    -Attributes: Learn how to handle class-level and instance-level attributes.
5. Exception Handling
    -Ability to handle common errors like file not found (FileNotFoundError), invalid input (ValueError), and I/O errors (IOError).
6. Command-Line Execution (Optional)
    -Familiarity with running Python scripts from the command line or terminal.
7. Saving and Loading Data
    -Basic knowledge of how to store and retrieve data, especially using file formats like plain text, CSV, or JSON, which is used in this code for storing expenses.

Work flow:
Step 1: Initialize the Budget
1.User Input:
    -The user defines an initial budget (e.g., $1000).
2.System Action:
    -The program initializes a BudgetManager object with the specified budget, setting spent = 0 and expenses = {} (an empty dictionary to hold categorized expenses).
3.Expected Outcome:
    -The budget is set, and the system is ready to track expenses.

Step 2: Add Expenses
1.User Input:
    -The user adds expenses to different categories (e.g., Groceries: $200, Rent: $600, Entertainment: $300).
2.System Action:
    -The add_expense() method is called.
    -It checks if the expense is valid (not negative).
    -It updates the category in the expenses dictionary or adds a new category if it doesn’t exist.
    -The system updates the total spent amount by adding the new expense.
3.Expected Outcome:
    -The expense is categorized and added to the running total.

Step 3: Calculate Remaining Budget
1.User Input:
    -The user requests to see how much of the budget is left.
2.System Action:
    -The calculate_remaining_budget() method is called.
    -The system calculates remaining_budget = budget - spent.
    -If remaining_budget is negative, a warning is displayed indicating that the user has overspent.
3.Expected Outcome:
    -The user sees the remaining balance, and a warning is issued if the budget has been exceeded.

Step 5: Reset the Budget
1.User Input:
        -The user wants to clear all expenses and start fresh.
2.System Action:
        -The reset_expenses() method is called.
        -The system sets spent = 0 and clears the expenses dictionary.
3.Expected Outcome:
        -All expenses are cleared, and the budget is reset to its initial value.

Step 6: Load Expenses from a File
1.User Input:
        -The user wants to load previously saved expenses from a file (e.g., expenses.txt).
2.System Action:
        -The load_from_file() method is called with the filename.
        -The system reads the file, retrieves the budget, total spent, and categorized expenses, and updates the program’s state accordingly.
3.Expected Outcome:
        -The budget, total spent, and categorized expenses are restored from the file.

Step 7: Error Handling and Warnings
1.Negative Expense Warning:
        -If the user tries to add a negative expense, an error message is displayed, and the system prevents the operation.

Future Plans:
1.Database Integration: Add a database to store authorized QR codes, access logs, and user information, allowing for more dynamic access control management.
2.Multi-Level Access Control: Implement different access levels (e.g., Admin, User, Guest) based on the QR code content, offering more granular control over permissions.
3.Email/SMS Notifications: Send alerts when access is denied or granted to a predefined email or phone number.