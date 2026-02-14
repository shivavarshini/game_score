name = input("Enter student name:")
math_marks = int(input("Enter Maths marks:"))
science_marks = int(input("Enter Science marks:"))
english_marks = int(input("Enter English marks:"))
print(f"Student Name:{name}")
if math_marks < 0 or math_marks > 100:
    print("Invalid marks entered")
elif science_marks < 0 or science_marks > 100:
    print("Invalid marks entered")
elif english_marks < 0 or english_marks > 100:
    print("Invalid marks entered")

total_marks = math_marks + science_marks + english_marks
print(f"Total Marks:{total_marks}")
average_marks = total_marks/3
print(f"Percentage:{average_marks:.2f}")
if average_marks >= 75:
    print("Status: PASS")
    print("Grade: A")
elif average_marks >= 60 and average_marks < 75:
    print("Status: PASS")
    print("Grade: B")
elif average_marks >= 40 and average_marks < 60:
    print("Status: FAIL")
