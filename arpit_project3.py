# Personal Expense Tracker

expenses = []
budget = float(input("Enter Monthly Budget: "))

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Expense
    if choice == "1":
        desc = input("Enter Description: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        date = input("Enter Date (DD-MM-YYYY): ")

        expense = {
            "description": desc,
            "category": category,
            "amount": amount,
            "date": date
        }

        expenses.append(expense)
        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses Found!")
        else:
            for e in expenses:
                print("\nDescription :", e["description"])
                print("Category    :", e["category"])
                print("Amount      :", e["amount"])
                print("Date        :", e["date"])

    # Category Summary
    elif choice == "3":
        summary = {}

        for e in expenses:
            cat = e["category"]

            if cat in summary:
                summary[cat] += e["amount"]
            else:
                summary[cat] = e["amount"]

        print("\nCategory Summary")
        for cat, total in summary.items():
            print(cat, ":", total)

    # Budget Report
    elif choice == "4":
        total = 0

        for e in expenses:
            total += e["amount"]

        remaining = budget - total

        print("\n===== BUDGET REPORT =====")
        print("Budget :", budget)
        print("Total Spent :", total)
        print("Remaining :", remaining)

        if total > budget:
            print("Budget Exceeded!")
        else:
            print("Within Budget")

    # Exit
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")