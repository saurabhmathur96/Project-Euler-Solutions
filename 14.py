def collatz(n):
    count = 1
    while n > 1:
        if n%2==0: n /= 2
        else : n = 3*n + 1
        count += 1
    return count

maximum = 0
i=0
n=0
while True:
    a = collatz(i)
    if a > maximum :
        maximum = a
        n = i
    i += 1
    if i>=1000000:
        break
print maximum
print n
