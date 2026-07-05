# Quiz and Examination System

questions = [
    ("Python is a ?", "A. Programming Language", "B. Game", "C. Browser", "D. OS", "A"),
    ("Which data type is immutable?", "A. List", "B. Dictionary", "C. Tuple", "D. Set", "C"),
    ("Which keyword is used for loop?", "A. repeat", "B. for", "C. loop", "D. run", "B"),
    ("Which function is used for input?", "A. print()", "B. output()", "C. input()", "D. read()", "C"),
    ("Which symbol is used for comments?", "A. //", "B. #", "C. /* */", "D. --", "B")
]

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

score = 0

print("\n===== QUIZ START =====")

for q in questions:
    print("\n" + q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    answer = input("Enter Answer (A/B/C/D): ").upper()

    if answer == q[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct Answer is", q[5])

total = len(questions)
percentage = (score / total) * 100

# Grade Calculation
if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B+"
elif percentage >= 50:
    grade = "B"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Name :", name)
print("Roll No :", roll)
print("Score :", score, "/", total)
print("Percentage :", percentage, "%")
print("Grade :", grade)

if percentage >= 50:
    print("Result : PASS")
else:
    print("Result : FAIL")