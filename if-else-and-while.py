# Ethan DeMougin
# if-else-and-while.py
# A program that determines if a student makes the Dean's List or Honor Roll by inputting a student's name and GPA.

while True:
  last_name = input("Enter student's last name (ZZZ to quit): ")

  first_name = input("Enter student's first name: ")

  gpa = float(input("Enter student's GPA: "))

  if gpa >= 3.25:
      print(f"{first_name} {last_name} has made the Honor Roll!")

  if gpa >= 3.5:
      print(f"{first_name} {last_name} has made the Dean's List!")

  if last_name.upper() == "ZZZ":
    print("Program ended."

  print()
