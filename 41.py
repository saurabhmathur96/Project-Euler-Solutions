import math
import itertools

def isprime(n):
    if n < 2 : return False
    if n % 2 == 0 : return False
    else :
        divisor = 3
        limit = math.sqrt(n)
        while (divisor <= limit): 
            if n % divisor == 0: return False
            divisor += 2
        return True

def pandigital_primes(length):
    t = [int(reduce(lambda x,y: x+str(y), num, '')) for num in itertools.permutations(range(1,length),length-1) ]
    return [i for i in t if isprime(i)]


def main():
    count = 10
    while count > 0:
        t = pandigital_primes(count)
        if t :
            print max(t)
            return
        count -=1

if __name__=='__main__':
    main()
    
