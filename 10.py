import math
def isprime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True
s = 0
for j in range(2,2000000):
    if (isprime(j) == 1) :
        s += j
print s
