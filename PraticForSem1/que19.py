# 6. Count the number of vowels in a word using while loop

word = input("Enter the Word: ")

counter = 0
index = 0 
while index < len(word):
    if word[index].lower() in ['a','e','i','o','u']:
        counter += 1
    index += 1
print(f"{counter} times vowels in {word}.")