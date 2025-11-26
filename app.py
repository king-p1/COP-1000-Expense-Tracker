# -------------------------------
# Personal Expense Tracker - Final Project
# -------------------------------

import datetime

# List to hold all expenses
expenses = []


def set_budget():
    """Allows the user to set a total budget."""
    while True:
        try:
            amount = float(input("Enter your total budget amount: $"))
            if amount < 0:
                print("Budget cannot be negative. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense():
    """Adds a new expense with name, amount, category, and date."""
    name = input("Enter expense name: ")
    category = input("Enter expense category: ")
    
    try:
        amount = float(input("Enter amount spent ($): "))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expense = {
            "name": name,
            "category": category,
            "amount": amount,
            "date": date
        }

        expenses.append(expense)
        print(f"Added '{name}' (${amount:.2f}) under category '{category}'.")
    
    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_expenses():
    """Displays all the stored expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n--- All Recorded Expenses ---")
    for e in expenses:
        print(f"{e['name']} - ${e['amount']:.2f} - {e['category']} - {e['date']}")
    print("-----------------------------")


def total_spent():
    """Calculates and displays the total amount spent."""
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal Spent: ${total:.2f}\n")
    return total


def view_by_category():
    """Shows spending organized by category."""
    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}

    for e in expenses:
        category = e['category']
        category_totals[category] = category_totals.get(category, 0) + e['amount']

    print("\n--- Expenses by Category ---")
    for cat, amount in category_totals.items():
        print(f"{cat}: ${amount:.2f}")
    print("-----------------------------")


def remove_expense():
    """Removes an expense by name."""
    name = input("Enter the expense name to remove: ")

    for e in expenses:
        if e['name'].lower() == name.lower():
            expenses.remove(e)
            print(f"Removed '{name}'.")
            return
    
    print("Expense not found.")


def clear_expenses():
    """Clears all recorded expenses."""
    expenses.clear()
    print("All expenses cleared.")


print("Welcome to the Personal Expense Tracker!")
budget = set_budget()

while True:
    print("\n*** Expense Tracker Menu ***")
    print("1) Add Expense")
    print("2) View All Expenses")
    print("3) View Total Spent")
    print("4) View Expenses by Category")
    print("5) Remove an Expense")
    print("6) Clear All Expenses")
    print("7) View Remaining Budget")
    print("8) Quit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        view_by_category()
    elif choice == "5":
        remove_expense()
    elif choice == "6":
        clear_expenses()
    elif choice == "7":
        remaining = budget - total_spent()
        print(f"Remaining Budget: ${remaining:.2f}")
    elif choice == "8":
        print("Goodbye! Thanks for using the Expense Tracker.")
        break
    else:
        print("Invalid choice. Try again.")
