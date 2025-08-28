l1=[x**2  for x in range(1,5)]
print(l1)
l2=[x.lower() for x in "hello world"]
print(l2)
l3=[int(x) for x in '1234']
print(l3)
l4=[x for x in 'abc^78%*(bcdjkb' if x.isalpha()]
print(l4) 