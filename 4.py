# -*- coding: cp1252 -*-
'''
Problem 3

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def reverse(s):
    return s[::-1]
def ispalindrome(n):
    return ( int(reverse(str(n))) == n )

palindromes=[]
largest = 0
for i in range(999,100,-1):
    for j in range(999,i,-1):
        product = i*j
        if ispalindrome(product) and product > largest:
            largest = product
print (largest)
