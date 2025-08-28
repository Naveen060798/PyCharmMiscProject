l1=[1,2,3,4,5,3,2,6,1]
rem=[ ]
for x in l1:
    if x not in rem:
        rem.append(x)
print(rem)