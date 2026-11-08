class Expense:

    def __init__(self, expense_id, description, amount, payer, category):
        # Store the expense details
        if type(expense_id) is not int or expense_id <= 0:
            raise ValueError("Expense ID must be a positive integer.")

        if type(amount) is not int or amount <= 0:
            raise ValueError("Amount must be a positive whole number.")

        if not all(isinstance(value, str) and value.strip()
                   for value in [description, payer, category]):
            raise ValueError("Description, payer and category cannot be empty.")

        self.expense_id = expense_id
        self.description = description.strip()
        self.amount = amount
        self.payer = payer.strip()
        self.category = category.strip()

