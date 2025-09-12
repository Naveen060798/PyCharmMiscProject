original={'a':1,'b':2,'c':1,'d':2,'e':3,'f':2}
invert={}
for key, value in original.items():
   if value not in invert:
       invert[value]={key}
   else:
       invert[value].add(key)
print(invert)
