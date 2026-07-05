# Library Management System

library = {}

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # Add Book
    if choice == "1":
        id = input("Enter Book ID: ")

        if id in library:
            print("Book Already Exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            library[id] = {
                "title": title,
                "author": author,
                "available": True
            }

            print("Book Added Successfully!")

    # Issue Book
    elif choice == "2":
        id = input("Enter Book ID: ")

        if id in library:
            if library[id]["available"]:
                library[id]["available"] = False
                print("Book Issued Successfully!")
            else:
                print("Book Already Issued!")
        else:
            print("Book Not Found!")

    # Return Book
    elif choice == "3":
        id = input("Enter Book ID: ")

        if id in library:
            library[id]["available"] = True
            print("Book Returned Successfully!")
        else:
            print("Book Not Found!")

    # Search Book
    elif choice == "4":
        id = input("Enter Book ID: ")

        if id in library:
            print("Title :", library[id]["title"])
            print("Author :", library[id]["author"])

            if library[id]["available"]:
                print("Status : Available")
            else:
                print("Status : Issued")
        else:
            print("Book Not Found!")

    # View All Books
    elif choice == "5":
        if len(library) == 0:
            print("No Books Available!")
        else:
            for id, book in library.items():
                print("\nID :", id)
                print("Title :", book["title"])
                print("Author :", book["author"])

                if book["available"]:
                    print("Status : Available")
                else:
                    print("Status : Issued")

    # Exit
    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")