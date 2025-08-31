Words={'plea','medical', 'decimal','listen','leap','silent','pale','enlist'}
result=set()
for x in Words:
    for y in Words:
        if x!=y and sorted(x)==sorted(y):
            pair=tuple(sorted((x,y)))
            result.add(pair)
for pair in result:
    print(pair)