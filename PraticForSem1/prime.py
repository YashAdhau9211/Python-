def is_prime(n):
    states = True
    if n < 2:
        states = False
    else:
        for i in range(2,n):
            if n % i == 0:
                states = False
    return states



for n in range(1,101):
    if is_prime(n):
        print(n,'',sep=',',end=' ')
print()