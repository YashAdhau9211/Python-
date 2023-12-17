str = input("Enter the Word: ")
count = 0
for i in str.lower():
    if i in ['a','e','i','o','u']:
        count+=1

print(f"{count} vowels are in {str}")