# ---------------------------
# Expense Tracker - Rough Draft
# ---------------------------

# A list to store all expense entries
expenses = []


# ---------------------------
# Function: Add a new expense
# ---------------------------
def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount ($): "))
        expenses.append({
            'name': name,
            'amount': amount
        })
        print(f"Added '{name}' for ${amount:.2f}")

    except ValueError:
        print("Invalid amount. Please enter a number.")


# ---------------------------
# Function: View all expenses
# ---------------------------
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Current Expenses ---")
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f}")


# ---------------------------
# Function: Calculate total spent
# ---------------------------
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")


# ---------------------------
# Function: Remove an expense by name
# ---------------------------
def remove_expense():
    name = input("Enter the name of the expense to remove: ")

    for expense in expenses:
        if expense['name'].lower() == name.lower():
            expenses.remove(expense)
            print(f"Removed '{name}'")
            break
    else:
        print("Expense not found.")


# ---------------------------
# Function: Clear all expenses
# ---------------------------
def clear_expenses():
    expenses.clear()
    print("All expenses have been cleared.")


# ---------------------------
# Main Menu (Loop)
# ---------------------------
while True:
    print("\n*** Expense Tracker Menu ***")
    print("1) Add Expense")
    print("2) View Expenses")
    print("3) View Total")
    print("4) Remove Expense")
    print("5) Clear All")
    print("6) Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        remove_expense()
    elif choice == '5':
        clear_expenses()
    elif choice == '6':
        print("Exiting Expense Tracker...")
        break
    else:
        print("Invalid option. Please try again.")
