from models import Expense
class ExpenseTracker:

    def __init__(self, participants, categories, expenses=None):
        self.participants = participants
        self.categories = categories
        self.expenses = expenses if expenses is not None else []