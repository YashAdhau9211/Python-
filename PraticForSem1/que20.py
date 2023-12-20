# 7. Check if a string is a palindrome using if condition

str = input("Enter the word: ")

if str == str[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

