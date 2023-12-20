# 4. Check if a word starts with a vowel or a consonant:

word = input("Enter the Word: ")
if word[0].lower() in ['a','e','i','o','u']:
    print(f"{word} start with a vowel.")
else:
    print(f"{word} start with a consonant.")