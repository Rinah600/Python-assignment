from models import Expense
class ExpenseTracker:

    def __init__(self, participants, categories, expenses=None):
        self.participants = participants
        self.categories = categories
        self.expenses = expenses if expenses is not None else []
    
    def add_expense(self, description, amount, payer, category):

        # Check that the payer is one of the participants
        if payer not in self.participants:
            raise ValueError("Payer must be one of the participants.")

        # Check that the category is allowed
        if category not in self.categories:
            raise ValueError("Invalid expense category.")

        # Generate the next expense ID
        expense_id = len(self.expenses) + 1

        # Create an expense object
        expense = Expense(expense_id, description, amount, payer, category)

        # Add the expense to the list
        self.expenses.append(expense)

        return expense