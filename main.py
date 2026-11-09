from pathlib import Path

from models import Expense
from tracker import ExpenseTracker
from storage import load_records, save_records


PARTICIPANTS = ("Maurice", "Alex")
CATEGORIES = ("Food", "Transport", "Utilities", "Other")

DATA_PATH = Path(__file__).resolve().parent / "data" / "expenses.json"


def read_description():
    while True:
        description = input("Description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")


def read_amount():
    while True:
        try:
            amount = int(input("Amount in whole UGX: "))

            if amount > 0:
                return amount

            print("Amount must be greater than zero.")

        except ValueError:
            print("Enter a whole number, such as 40000.")


def choose_option(title, options):
    print(f"\n{title}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Choose a number: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Choose one of the numbers shown.")

        except ValueError:
            print("Enter a number.")


def main():
    try:
        records = load_records(DATA_PATH)
        expenses = []

        for record in records:
            expenses.append(Expense.from_dict(record))

        tracker = ExpenseTracker(
            PARTICIPANTS,
            CATEGORIES,
            expenses,
        )

    except (ValueError, OSError) as error:
        print(f"Could not load expenses: {error}")
        return

    while True:
        print("\nSHARED EXPENSE TRACKER")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View summary")
        print("4. View category totals")
        print("5. Show settlement")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = read_description()
            amount = read_amount()
            payer = choose_option("Who paid?", PARTICIPANTS)
            category = choose_option("Category:", CATEGORIES)

            try:
                tracker.add_expense(
                    description,
                    amount,
                    payer,
                    category,
                )

            except ValueError as error:
                print(f"Could not add expense: {error}")
                continue

            try:
                save_records(DATA_PATH, tracker.to_records())

            except (ValueError, OSError) as error:
                print(f"Expense was not saved: {error}")
                print("Closing the application. Please fix the problem.")
                return

            print("Expense saved.")

        elif choice == "2":
            expenses = tracker.list_expenses()

            if not expenses:
                print("No expenses recorded yet.")

            for expense in expenses:
                print(
                    f"#{expense.id} | {expense.description} | "
                    f"{expense.amount:,} UGX | "
                    f"{expense.payer} | {expense.category}"
                )

        elif choice == "3":
            print(f"\nTotal spending: {tracker.total_spending():,} UGX")

            for person, amount in tracker.totals_by_payer().items():
                print(f"{person} paid: {amount:,} UGX")

        elif choice == "4":
            print("\nSPENDING BY CATEGORY")

            for category, amount in tracker.totals_by_category().items():
                print(f"{category}: {amount:,} UGX")

        elif choice == "5":
            settlement = tracker.settlement()

            if settlement is None:
                print("Neither person owes anything.")

            else:
                print(
                    f"{settlement['from']} owes "
                    f"{settlement['to']} "
                    f"{settlement['amount']:,} UGX."
                )

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Choose an option from 1 to 6.")


if __name__ == "__main__":
    main()