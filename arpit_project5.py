# Inventory Management System

inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    # Add Product
    if choice == "1":
        pid = input("Enter Product ID: ")

        if pid in inventory:
            print("Product ID Already Exists!")
        else:
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            reorder = int(input("Enter Reorder Level: "))

            inventory[pid] = {
                "name": name,
                "category": category,
                "price": price,
                "qty": qty,
                "reorder": reorder
            }

            print("Product Added Successfully!")

    # Stock In
    elif choice == "2":
        pid = input("Enter Product ID: ")

        if pid in inventory:
            add_qty = int(input("Enter Quantity to Add: "))
            inventory[pid]["qty"] += add_qty
            print("Stock Updated!")
        else:
            print("Product Not Found!")

    # Stock Out
    elif choice == "3":
        pid = input("Enter Product ID: ")

        if pid in inventory:
            remove_qty = int(input("Enter Quantity to Remove: "))

            if remove_qty <= inventory[pid]["qty"]:
                inventory[pid]["qty"] -= remove_qty
                print("Stock Removed!")
            else:
                print("Not Enough Stock!")
        else:
            print("Product Not Found!")

    # View Inventory
    elif choice == "4":
        if len(inventory) == 0:
            print("No Products Available!")
        else:
            for pid, product in inventory.items():
                print("\nProduct ID :", pid)
                print("Name       :", product["name"])
                print("Category   :", product["category"])
                print("Price      :", product["price"])
                print("Quantity   :", product["qty"])

    # Low Stock Alert
    elif choice == "5":
        print("\nLow Stock Products:")

        for pid, product in inventory.items():
            if product["qty"] <= product["reorder"]:
                print(product["name"], "- Quantity:", product["qty"])

    # Report
    elif choice == "6":
        total_value = 0

        for product in inventory.values():
            total_value += product["price"] * product["qty"]

        print("\n===== INVENTORY REPORT =====")
        print("Total Products :", len(inventory))
        print("Total Stock Value :", total_value)

    # Exit
    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")