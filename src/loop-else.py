# -*- coding: utf-8 -*-

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number.')
else:
    print("Else de um for: significa que loop foi executado até o final sem encontrar um break para ele próprio.")
