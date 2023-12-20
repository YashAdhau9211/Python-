# 2. Check if a student's grade is 'A', 'B', or 'C':

grade = input("Enter the Grade: ")
if grade.lower() in ['a','b','c']:
    print("Pass.")
else:
    print("Fail.")