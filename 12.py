from math import sqrt
def factors(n):    
    return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))

def main():
    triangleNumbers = [0]
    counter = 0
    while(True):
        counter += 1
        triangleNumbers.append(triangleNumbers[counter-1]+counter)
        if factors(triangleNumbers[counter]) >= 500:
            print triangleNumbers[counter]
            return

if __name__ == '__main__':
    main()
