# Student Management System
# Create the empty dictionary
students = {}

while True:
    print("\n===== MENU =====")
    print("1. Add New Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")
    # Takes user choice
    choice = input("Enter Choice: ")
    # Option 1: Add new Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student Added Successfully!")
    # Option 2: Update Marks
    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            new_marks = int(input("Enter New Marks: "))
            students[roll].update({"marks": new_marks})
            print("Marks Updated!")
        else:
            print("Student Not Found!")
    # Option 3: Search Student
    elif choice == "3":
        roll = input("Enter Roll Number: ")

        student = students.get(roll)

        if student:
            print(student)
        else:
            print("Student Not Found!")
    # Option 4: Display all Elements
    elif choice == "4":
        for roll, details in students.items():
            print("Roll No:", roll)
            print(details)
    # Option 5: Remove Student
    elif choice == "5":
        roll = input("Enter Roll Number: ")

        removed = students.pop(roll, None)

        if removed:
            print("Student Removed!")
        else:
            print("Student Not Found!")
    # Option 6: Exit program
    elif choice == "6":
        print("Exiting Program...")
        break
    # Invalid Choice
    else:
        print("Invalid Choice!")