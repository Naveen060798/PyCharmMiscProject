import re
str1="Time is the most valuable thing we have, and once lost, it never returns"
str2="We never get time back once it's gone- it's truly the most valuable resource"
w1=re.findall(r'\w+',str1.lower())
w2=re.findall(r'\w+',str2.lower())
ws1=set(w1)
ws2=set(w2)
common=ws1&ws2
unique=ws1|ws2
plaigarism=len(common)/len(unique)
if plaigarism >= 0.5:
    print('plaigarism')
else:
    print('Potential Plaigarism')