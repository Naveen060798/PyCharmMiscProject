import calendar as cal
def month():
    count=1
    while True:
        name=cal.month_name[count]
        yield name
        count=count%12+1
m=month()
print(next(m))
print(next(m))
print(next(m))