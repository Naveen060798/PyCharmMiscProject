users=['john','bob','alex','alice','charlie','john','alex','alice', 'john','alex']
login={ }
for x in users:
    if x in login:
        login[x]+=1
    else:
        login[x]=1
for user,count in login.items():
    print(f"{user} : {count} login")