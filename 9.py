import timeit
def main():
 t1 = timeit.default_timer()
 print ('start time = ' + str(t1))
 for a in range(1,1000):
     for b in range(a+1,1000):
         c=b+1
         while (a*a + b*b > c*c):
             c += 1
         if a*a + b*b == c*c and c <= 1000 and a+b+c == 1000 :
             print ('ans = '+str(a*b*c))
             t2 = timeit.default_timer()
             print ('stop time = ' + str(t2))
             print('time taken =' + str(t2-t1))
             return
if __name__ == '__main__':
    main()
