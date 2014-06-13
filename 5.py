'''
Problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def hcf( x,y ):
    '''HCF using euclid's formula'''
    while y:
        x, y = y, x%y
    return x

def lcm( x,y ):
    '''since LCM * HCF = product of numbers'''
    lcm = x*y/hcf(x,y)
    return lcm
nums = range(1,21)

print reduce(lcm,nums)
