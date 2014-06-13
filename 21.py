from time import *

def d (n) :
    return sum([i for i in range(1,n//2 +1) if n%i==0])

start = clock()
total = 0
for i in range(1,10000):
    x = d(i)
    y = d(x)
    if i == y and i != x :
        total += x
print total
print clock() -start
