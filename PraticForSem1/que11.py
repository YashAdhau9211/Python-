str = input("Word: ")
new_word = ""
for i in range(0 , len(str) , 2):
     new_word += str[i]

print(new_word)