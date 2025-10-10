
expenses = []   

def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter expense amount ($): "))
        expenses.append({'name': name, 'amount': amount})
        print(f"✅ Added '{name}' for ${amount:.2f}")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Current Expenses ---")
    for e in expenses:
        print(f"{e['name']}: ${e['amount']:.2f}")

def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print(f"\n Total Expenses: ${total:.2f}")

def remove_expense():
    name = input("Enter the name of the expense to remove: ")
    for e in expenses:
        if e['name'].lower() == name.lower():
            expenses.remove(e)
            print(f"Removed '{name}'")
            break
    else:
        print("❌ Expense not found.")

def clear_expenses():
    expenses.clear()
    print("All expenses cleared!")

# Main Menu Loop
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
        print("You quit Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")

