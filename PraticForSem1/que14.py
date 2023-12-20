# 1. Check if a number is divisible by both 2 and 3

num = int(input("Enter the Number: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by 2 and 3.")
else:
    print(f"{num} is not divisible by 2 and 3.")