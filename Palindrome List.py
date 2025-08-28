l=input('enter number with spaces: ')
ll=l.split()
rev=ll[::-1]
if ll==rev:
    print('YES',rev)
else:
    print('NO')

