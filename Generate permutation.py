import itertools as it
l=['A','B','C','D']
per=it.permutations(l, r=2)
per=list(per)
print(per)
for t in per:
    print(t)
