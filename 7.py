'''
Problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from math import sqrt
def isprime(n):
    if n == 2 : return True
    if n%2 == 0: return False
    for i in range(3, int(sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

i = 2
count = 0
LIMIT = 10001
while (count<LIMIT):
    if isprime(i):
        count += 1
    i += 1
print i-1
