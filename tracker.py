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
    
    # Lists all expenses
    def list_expenses(self):
        return self.expenses.copy()
    
    # Calculates the total spending
    def total_spending(self):
        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total
    
    
    # Calculates the total spending by each participant
    def totals_by_payer(self):
        totals = {}

        # Start each participant's total at zero
        for participant in self.participants:
            totals[participant] = 0

        # Add each expense to the person who paid
        for expense in self.expenses:
            totals[expense.payer] += expense.amount

        return totals
    
    def totals_by_category(self):
        totals = {}
        # Give every category an initial value of zero
        for category in self.categories:
            totals[category] = 0
        # Add the expense amount to its category
        for expense in self.expenses:
            totals[expense.category] += expense.amount

        return totals
    
    def settlement(self):

        totals = self.totals_by_payer()

        person_a = self.participants[0]
        person_b = self.participants[1]

        total = self.total_spending()

        # Calculate each person's fair share
        fair_share = total / 2

        # Calculate how much person A paid above or below their share
        balance = totals[person_a] - fair_share

        # If both people contributed equally
        if balance == 0:
            return None

        # If person A paid more
        if balance > 0:
            return {
                "from": person_b,
                "to": person_a,
                "amount": balance
            }

        # If person B paid more
        return {
            "from": person_a,
            "to": person_b,
            "amount": abs(balance)
        }
        
    def to_records(self):
        records = []

        for expense in self.expenses:
            records.append(expense.to_dict())

        return records