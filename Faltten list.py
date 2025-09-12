def flatten(l):
    for x in l:
        if hasattr(x,'__iter__'):
            yield from flatten(x)
        else:
            yield x
l=[1,2,[3,4,[5,6,7],8],9,[10,11,12,13]]

flat=flatten(l)
flat_list=list(flat)
print(flat_list)