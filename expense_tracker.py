import datetime

# Initialize an empty list to store expenses
expenses = []

def add_expense():
    """Add a new expense."""
    category = input("Enter expense category (e.g., Food, Transport, etc.): ").strip()
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.date.today().isoformat()
    expenses.append({"category": category, "amount": amount, "date": date})
    print(f"Expense added: {category}, {amount} on {date}.")

def view_expenses():
    """View all expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['category']}: ${expense['amount']:.2f}")
    print("----------------------")

def summary_by_category():
    """Show a summary of expenses by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense Summary by Category ---")
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    print("------------------------------------")

def calculate_total():
    """Calculate and display the total spending."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spending: ${total:.2f}")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Calculate total spending")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
