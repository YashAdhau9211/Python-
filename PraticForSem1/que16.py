# 3.Check if a year is a leap year and a multiple of 5:

year = int(input("Enter the Year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    if year % 5 == 0:
        print(f"{year} is a Leap year and multiple of 5.")
else:
    print(f"{year} is not a Leap year.")