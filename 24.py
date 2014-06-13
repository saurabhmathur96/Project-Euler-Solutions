import itertools

print ''.join(str(c) for c in (list(itertools.permutations(range(10))))[999999])
