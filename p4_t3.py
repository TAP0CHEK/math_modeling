import numpy as np
import random as random
n = 10

def mpl(a):
    s = 1
    for i in range(n):
        s *= a[i]
    return s

arr = [0] * n
for i in range(n):
    arr[i] = int(rnd.random() * 100)
print(mpl(arr), arr)