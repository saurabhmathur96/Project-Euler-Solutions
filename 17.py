from num2words import num2words
num = 0
for i in range(1,1001) :
    s = num2words(i)
    num += len(s) - s.count(" ")  - s.count("-")
print (num)
