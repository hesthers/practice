#Fibonacci sequence 

import numpy as np
def fibo(n):
    l = np.zeros(n)
    l[1] = 1
    for _ in range(2, n):
        l[_] = l[_-1] + l[_-2]
    return l

fibo(8)
