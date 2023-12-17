str1 = input("Enter the first word: ")
str2 = input("Enter the Second word: ")

if sorted(str1) == sorted(str2):
    print("The words are in Anagram forms.")
else:
    print("The words are not in Anagram forms.")