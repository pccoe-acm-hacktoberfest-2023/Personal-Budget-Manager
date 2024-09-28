class BudgetManager:
    def __init__(self, budget):
        self.budget = budget
        self.spent = 0
        self.expenses = {}  # Keeps track of expense categories

    def add_expense(self, category, amount):
        # Add new expense to the category
        if amount < 0:  # Ensure expenses cannot be negative
            print(f"Error: Cannot add negative expense: {amount}")
            return
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.spent += amount
        print(f"Added {amount} to {category}. Total spent: {self.spent}")

    def calculate_remaining_budget(self):
        remaining_budget = self.budget - self.spent
        print(f"Remaining budget: {remaining_budget}")

        # Check if the user overspent
        if remaining_budget < 0:
            print("Warning: You have overspent your budget!")

    def reset_expenses(self):
        self.spent = 0
        self.expenses.clear()
        print("Expenses have been reset.")

    def save_to_file(self, filename):
        # Saves the expenses to a file
        try:
            with open(filename, "w") as file:
                file.write(f"Budget: {self.budget}\n")
                file.write(f"Spent: {self.spent}\n")
                for category, amount in self.expenses.items():
                    file.write(f"{category}: {amount}\n")
                print(f"Expenses saved to {filename}")
        except:
            print("Error: Could not save to file.")

    def load_from_file(self, filename):
        # Loads the expenses from a file
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                self.budget = int(lines[0].split(": ")[1].strip())
                self.spent = int(lines[1].split(": ")[1].strip())
                self.expenses = {}
                for line in lines[2:]:
                    category, amount = line.split(": ")
                    self.expenses[category] = int(amount.strip())
            print(f"Expenses loaded from {filename}")
        except:
            print("Error: Could not load from file.")


# Create an instance of BudgetManager with a budget of 1000
budget_manager = BudgetManager(1000)

# Add expenses
budget_manager.add_expense("Groceries", 200)
budget_manager.add_expense("Entertainment", 300)
budget_manager.add_expense("Rent", 600)

# Check remaining budget
budget_manager.calculate_remaining_budget()

# Save expenses to a file
budget_manager.save_to_file("expenses.txt")

# Reset and reload from file
budget_manager.reset_expenses()
budget_manager.load_from_file("expenses.txt")
budget_manager.calculate_remaining_budget()

# Task: Fix the code
