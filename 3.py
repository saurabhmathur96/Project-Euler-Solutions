'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

num = 600851475143
if num % 2 == 0:
    n /= 2
    largest = n
    while n %2 == 0:
        n /= 2
else :
    largest = 1

i = 1
while num >1:
    i += 2
    if num % i == 0:
        num /= i
        largest = i
        while num%i == 0:
            num /= i
print largest
