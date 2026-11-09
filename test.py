from tracker import ExpenseTracker

participants = ("Maurice", "Alex")
categories = ("Food", "Transport", "Utilities", "Other")

tracker = ExpenseTracker(participants, categories)

# Add expenses
tracker.add_expense("Dinner", 40000, "Maurice", "Food")
tracker.add_expense("Taxi", 20000, "Alex", "Transport")

# List expenses
print("\nALL EXPENSES")
for expense in tracker.list_expenses():
    print(expense.to_dict())

# Total spending
print("\nTOTAL SPENDING")
print(tracker.total_spending())

# Totals by payer
print("\nTOTALS BY PAYER")
print(tracker.totals_by_payer())

# Totals by category
print("\nTOTALS BY CATEGORY")
print(tracker.totals_by_category())

# Settlement
print("\nSETTLEMENT")
print(tracker.settlement())

# Convert expenses into dictionaries
print("\nEXPENSE RECORDS")
print(tracker.to_records())