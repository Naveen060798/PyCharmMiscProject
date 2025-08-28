hours=input('Enter number of hours: ')
wages=int(input('Enter wage /hr: '))
hours=hours.split()    #coverts to string of list
weekly_hr=[int(x) for x in hours]    #converts to list of elements
total_hr=sum(weekly_hr)      #calculates total hrs in a week
if total_hr<=40:
    total_wage=total_hr*wages
else:
    ot=total_hr-40
    total_wage=40*wages+ot*wages*1.5
print('total_wage', total_wage)

