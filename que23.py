num = 123456
rever_num = 0

while num > 0:
    rem = num % 10 
    rever_num = rever_num*10 + rem
    num = num // 10
print(rever_num)