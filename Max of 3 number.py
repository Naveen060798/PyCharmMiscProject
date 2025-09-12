def max3(a,b,c,/):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print("Maxi,um of 3 number:",max3(30,500,321))