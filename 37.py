
def isprime(n):
    
    if n < 2 : return False
    if n & 1 == 0 : return n == 2
    idx = 3
    while idx*idx <= n:
        if n%idx == 0 : return False
        idx += 2
    return True

def truncate_left(n):
    t = list(str(n))
    lim = len(t)
    i = 1
    while i < lim:
        if not isprime(int(''.join(t[i:]))): return False
        i += 1
    return True

def truncate_right(n):
    t = list(str(n))
    lim = len(t)
    i = 1
    while i < lim:
        if not isprime(int(''.join(t[:(-i)]))): return False
        i += 1
    return True

def istruncatable(n):
    return truncate_left(n) and truncate_right(n)


limit = 1000000

def f(n):
    for i in xrange(n):
        if isprime(i) :
            if istruncatable(i):
                yield i

print sum(f(limit)) - 2 - 3 - 5 -7
