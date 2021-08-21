#Finding out whether the number is a lunar year when entering the number

def lunar_year(num):
        if 1 <= num <= 3000:
            if (num % 4 == 0) | (num % 100 != 0) & (num % 400 == 0):
                return print('It is a lunar year.')
            else:
                return print('It is not a lunar year.')
        else:
            print('wrong number')

year = int(input('Enter the year '))
lunar_year(year)


#Fibonacci sequence 

import numpy as np
def fibo(n):
    l = np.zeros(n)
    l[1] = 1
    for _ in range(2, n):
        l[_] = l[_-1] + l[_-2]
    return l

fibo(8)

