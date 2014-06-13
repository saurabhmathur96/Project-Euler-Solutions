LIMIT = 1000000
d = ''.join([str(i) for i in range(LIMIT)])
ans = 1
idx = LIMIT
while idx > 0 :
    ans *= int(d[idx])
    idx //= 10
print ans
